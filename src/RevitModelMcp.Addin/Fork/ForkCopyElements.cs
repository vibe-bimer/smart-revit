using Autodesk.Revit.DB;
using RevitModelMcp.Capture;
using RevitModelMcp.Core.Control;
using RevitModelMcp.Core.Fork;

namespace RevitModelMcp.Control.Fork;

/// <summary>
/// Copies elements inside one model and keeps their hosts: the document-to-document overload rehosts a
/// hosted element onto the copy of its host, which the point overload does not. A hosted element travels
/// with its host in the same batch, because Revit deletes a hosted element whose host is missing when the
/// paste finishes. Copies destroy nothing, so a refusal is reported per element instead of aborting the
/// request. See docs/modeling-tools.md.
/// </summary>
internal static class ForkCopyElements
{
    /// <summary>Whether the request names at least one element, which every copy needs.</summary>
    internal static void Validate(ActionJobContract action) =>
        ForkLookup.Require(action.ElementIds is { Count: > 0 }, "elementIds must hold at least one element id.");

    /// <summary>
    /// Refuses bad input before the transaction opens: an element that does not exist, a target level the
    /// model does not hold, or a hosted element whose host the request left out.
    /// </summary>
    internal static void Check(Document document, ActionJobContract action)
    {
        Validate(action);
        if (!string.IsNullOrWhiteSpace(action.Options.TargetLevel)) _ = Target(document, action);
        RefuseMissingHosts(document, action.ElementIds!);
    }

    /// <summary>Copies the addressed elements and reports the old to new pairing.</summary>
    internal static ActionResultData Copy(Document document, ActionJobContract action, List<ElementId> ids)
    {
        Validate(action);
        var options = action.Options;
        var target = string.IsNullOrWhiteSpace(options.TargetLevel) ? null : Target(document, action);
        RefuseMissingHosts(document, ids.Select(RevitValueReader.GetId).ToList());

        var ineligible = new List<ForkIneligibleElement>();
        var mapping = new List<ForkIdPair>();
        var made = new List<ElementId>();
        var mismatches = 0;
        foreach (var component in Components(document, ids))
        {
            var delta = Offset(document, component, target, options);
            using var copy = new SubTransaction(document);
            copy.Start();

            // The commit is inside the try on purpose: Revit regenerates the model there, and a
            // regeneration that cannot place one of the copies throws the same way the paste does.
            var pairs = new List<ForkIdPair>();
            var groupMismatches = 0;
            var created = new List<ElementId>();
            try
            {
                created = ElementTransformUtils
                    .CopyElements(document, component, document, Transform.CreateTranslation(delta), PasteOptions())
                    .ToList();
                Pair(document, component, created, delta, pairs, ref groupMismatches);
                copy.Commit();
            }
            catch (Exception exception) when (exception is not OperationCanceledException)
            {
                // One component at a time keeps the refusal on the elements it belongs to; copying
                // removes nothing, so the rest of the request can still go ahead.
                foreach (var id in component)
                {
                    ineligible.Add(new ForkIneligibleElement
                    {
                        Id = RevitValueReader.GetId(id),
                        Kind = "copy",
                        Reason = exception.Message
                    });
                }

                if (copy.GetStatus() == TransactionStatus.Started) copy.RollBack();
                continue;
            }

            made.AddRange(created);
            mapping.AddRange(pairs);
            mismatches += groupMismatches;
        }

        if (mapping.Count == 0 && ineligible.Count > 0)
        {
            throw new InvalidOperationException(
                $"Revit copied none of the {ids.Count} addressed elements. {Describe(ineligible)}");
        }

        return new ActionResultData
        {
            Count = made.Count,
            ForkOutcome = new ForkOutcome
            {
                IdMapping = mapping.Count == 0 ? null : mapping,
                IdMappingVerified = mismatches == 0 && mapping.Count == ids.Count,
                MappingMismatches = mismatches == 0 ? null : mismatches,
                Ineligible = ineligible.Count == 0 ? null : ineligible,
                IneligibleCount = ineligible.Count == 0 ? null : ineligible.Count,
                IneligibleKinds = ineligible.Count == 0 ? null : [new ForkCount { Kind = "copy", Count = ineligible.Count }]
            },
            Verification = new ActionVerification { Changed = made.Select(RevitValueReader.GetId).ToList() }
        };
    }

    /// <summary>The level a targetLevel copy measures its rise from.</summary>
    private static Level Target(Document document, ActionJobContract action) =>
        ForkLookup.Level(document, action.Options.TargetLevel!);

    /// <summary>
    /// A hosted element needs its host in the same request: Revit deletes a hosted copy that finds no
    /// host, and a silent deletion is worse than a refusal that names the pair.
    /// </summary>
    private static void RefuseMissingHosts(Document document, List<long> ids)
    {
        var named = ids.ToHashSet();
        var missing = new List<string>();
        foreach (var id in ids)
        {
            var elementId = ForkLookup.CreateId(id);
            if (document.GetElement(elementId) is not FamilyInstance instance || instance.Host is not { } host) continue;
            var hostId = RevitValueReader.GetId(host.Id);
            if (hostId == id || named.Contains(hostId)) continue;
            missing.Add($"{id} (hosted on {hostId})");
        }

        if (missing.Count == 0) return;
        throw new ArgumentException(
            $"elementIds must also hold the host of every hosted element: {string.Join(", ", missing)}. "
            + "A hosted copy that cannot find its host is deleted when the paste finishes.");
    }

    /// <summary>
    /// Groups the elements that must be copied together: a hosted element travels with its host, and a
    /// host with its own host, so a wall and the doors on it are one batch.
    /// </summary>
    private static List<List<ElementId>> Components(Document document, List<ElementId> ids)
    {
        var byId = ids.ToDictionary(RevitValueReader.GetId);
        var parent = new Dictionary<long, long>();
        long Find(long id)
        {
            while (parent.TryGetValue(id, out var next) && next != id) id = next;
            return id;
        }

        foreach (var id in ids) parent[RevitValueReader.GetId(id)] = RevitValueReader.GetId(id);
        foreach (var id in ids)
        {
            if (document.GetElement(id) is not FamilyInstance instance || instance.Host is not { } host) continue;
            var mine = RevitValueReader.GetId(id);
            var theirs = RevitValueReader.GetId(host.Id);
            if (!byId.ContainsKey(theirs) || theirs == mine) continue;
            var root = Find(mine);
            var other = Find(theirs);
            if (root != other) parent[root] = other;
        }

        return ids.GroupBy(id => Find(RevitValueReader.GetId(id)))
                  .Select(group => group.ToList())
                  .ToList();
    }

    /// <summary>
    /// The translation for one batch: the level difference when a target level is named, plus the offsets
    /// the caller gave. A batch that spans more than one level has no single height to measure from.
    /// </summary>
    private static XYZ Offset(Document document, List<ElementId> component, Level? target, ForkOptions options)
    {
        var dz = ForkLookup.Millimeters(options.DzMm ?? 0);
        if (target is not null)
        {
            var levels = component
                .Select(id => document.GetElement(id) is { } element ? document.GetElement(element.LevelId) as Level : null)
                .Where(level => level is not null)
                .Select(level => level!)
                .GroupBy(level => level.Elevation)
                .ToList();
            if (levels.Count != 1)
            {
                var names = string.Join(", ", component.Select(RevitValueReader.GetId));
                throw new ArgumentException(
                    $"targetLevel needs one source level, but elements {names} sit on "
                    + (levels.Count == 0 ? "no level" : $"{levels.Count} different levels")
                    + ". Give dz_mm instead, or copy one level at a time.");
            }

            dz += target.Elevation - levels[0].Key;
        }

        return new XYZ(ForkLookup.Millimeters(options.DxMm ?? 0), ForkLookup.Millimeters(options.DyMm ?? 0), dz);
    }

    /// <summary>
    /// CopyElements returns the new ids in no promised order and gives no mapping, so each copy is paired
    /// with its source by category, type and the position the translation predicts. A pair that cannot be
    /// proven keeps the mapping unverified instead of guessing.
    /// </summary>
    private static void Pair(
        Document document,
        List<ElementId> sources,
        List<ElementId> created,
        XYZ delta,
        List<ForkIdPair> mapping,
        ref int mismatches)
    {
        var remaining = new List<ElementId>(created);
        foreach (var source in sources)
        {
            var original = document.GetElement(source);
            var match = remaining.FirstOrDefault(candidate => Agrees(original, document.GetElement(candidate), delta));
            if (match is null)
            {
                mismatches++;
                continue;
            }

            remaining.Remove(match);
            mapping.Add(new ForkIdPair { Old = RevitValueReader.GetId(source), New = RevitValueReader.GetId(match) });
        }

        mismatches += remaining.Count;
    }

    private static bool Agrees(Element? original, Element? copy, XYZ delta)
    {
        if (original is null || copy is null) return false;
        if (original.Category?.Id != copy.Category?.Id) return false;
        if (original.GetTypeId() != copy.GetTypeId()) return false;

        // The location line and the insertion point survive a paste exactly; only the geometry may
        // move, because Revit re-resolves joins and attachments at the new place. A wall that gains a
        // join at its new spot has a different bounding box and would never pair by position alone.
        if (original.Location is LocationCurve mine && copy.Location is LocationCurve theirs)
        {
            // A wall keeps its location line on the level it was drawn on, so a copy that rises by
            // dz still reports the old z on that line; the rise lives in the bounding box instead.
            // Comparing the endpoints flat keeps a raised copy pairing with its source.
            var forward = Flat(mine.Curve.GetEndPoint(0) + delta, theirs.Curve.GetEndPoint(0))
                && Flat(mine.Curve.GetEndPoint(1) + delta, theirs.Curve.GetEndPoint(1));
            var backward = Flat(mine.Curve.GetEndPoint(0) + delta, theirs.Curve.GetEndPoint(1))
                && Flat(mine.Curve.GetEndPoint(1) + delta, theirs.Curve.GetEndPoint(0));
            return forward || backward;
        }

        if (original.Location is LocationPoint minePoint && copy.Location is LocationPoint theirPoint)
        {
            return Flat(minePoint.Point + delta, theirPoint.Point);
        }

        var before = original.get_BoundingBox(null);
        var after = copy.get_BoundingBox(null);
        if (before is null || after is null) return true;
        return Flat(before.Min + delta, after.Min);
    }

    /// <summary>
    /// Compares two points on the plane. A wall keeps its location line on the level it was drawn on,
    /// so the vertical part of a copy never shows up on that line; the one-to-one pairing inside a
    /// single batch is what keeps two identical walls apart.
    /// </summary>
    private static bool Flat(XYZ expected, XYZ actual)
    {
        const double tolerance = 1e-3;
        return Math.Abs(expected.X - actual.X) < tolerance && Math.Abs(expected.Y - actual.Y) < tolerance;
    }

    /// <summary>
    /// The paste options every copy needs: without a duplicate-name handler Revit asks the question in a
    /// modal dialog, which blocks an unattended session for good.
    /// </summary>
    private static CopyPasteOptions PasteOptions()
    {
        var options = new CopyPasteOptions();
        options.SetDuplicateTypeNamesHandler(new UseDestinationTypes());
        return options;
    }

    private static string Describe(List<ForkIneligibleElement> ineligible)
    {
        const int shown = 5;
        var names = ineligible.Take(shown).Select(item => $"{item.Id}: {item.Reason}");
        var more = ineligible.Count > shown ? $" (+{ineligible.Count - shown} more)" : string.Empty;
        return string.Join("; ", names) + more;
    }

    /// <summary>Answers Revit's duplicate-type question with the types the model already has.</summary>
    private sealed class UseDestinationTypes : IDuplicateTypeNamesHandler
    {
        public DuplicateTypeAction OnDuplicateTypeNamesFound(DuplicateTypeNamesHandlerArgs args) =>
            DuplicateTypeAction.UseDestinationTypes;
    }
}
