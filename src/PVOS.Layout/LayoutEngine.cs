using PVOS.Core;

namespace PVOS.Layout;

public sealed class LayoutEngine
{
    public LayoutResult Generate(LayoutRequest? request)
    {
        var errors = Validate(request);
        if (request is null || errors.Count > 0)
            return Rejected(request, errors);

        var partition = request.Geometry.Partitions.Single(item => item.Id == request.SelectedPartitionId);
        var transform = new AxisTransform(request.Axis);
        var localBoundary = transform.ToLocal(new Polygon2D(partition.Boundary.Vertices.ToArray()));
        var boundingBox = Geometry2D.BoundingBox(localBoundary);
        var module = request.Module;

        var minX = boundingBox.MinX + module.EdgeMarginMm;
        var minY = boundingBox.MinY + module.EdgeMarginMm;
        var maxX = boundingBox.MaxX - module.EdgeMarginMm;
        var maxY = boundingBox.MaxY - module.EdgeMarginMm;

        var panels = new List<Panel>();
        var rows = new List<RowDecision>();
        var candidateIndex = 0;

        if (minX + module.EffectiveWidthMm <= maxX + Geometry2D.Epsilon
            && minY + module.EffectiveLengthMm <= maxY + Geometry2D.Epsilon)
        {
            var rowNumber = 0;
            for (var y = minY;
                 y + module.EffectiveLengthMm <= maxY + Geometry2D.Epsilon;
                 y += module.RowPitchMm)
            {
                rowNumber++;
                var row = new RowDecision(rowNumber);
                var columnNumber = 0;

                for (var x = minX;
                     x + module.EffectiveWidthMm <= maxX + Geometry2D.Epsilon;
                     x += module.ColumnPitchMm)
                {
                    columnNumber++;
                    candidateIndex++;
                    var candidate = new Rect2D(
                        x,
                        y,
                        x + module.EffectiveWidthMm,
                        y + module.EffectiveLengthMm);

                    if (!Geometry2D.RectangleFullyInside(candidate, localBoundary))
                    {
                        row.Rejected++;
                        continue;
                    }

                    row.Accepted++;
                    var placementOrder = panels.Count + 1;
                    panels.Add(new Panel(
                        $"PNL-{placementOrder:000000}",
                        placementOrder,
                        candidateIndex,
                        rowNumber,
                        columnNumber,
                        candidate.Corners.Select(transform.ToGlobal).ToArray()));
                }

                rows.Add(row);
            }
        }

        var warnings = BuildWarnings(request.Id, panels.Count, candidateIndex, rows);
        return new LayoutResult(
            request.Id,
            partition.Id,
            PlacementStatus.Accepted,
            panels,
            panels.Count * module.RatedPowerWp / 1000.0,
            warnings,
            []);
    }

    private static List<PlacementMessage> Validate(LayoutRequest? request)
    {
        var errors = new List<PlacementMessage>();
        if (request is null)
        {
            errors.Add(Error("PLC_REQUEST_INVALID", "A placement request is required."));
            return errors;
        }

        if (string.IsNullOrWhiteSpace(request.Id))
            errors.Add(Error("PLC_REQUEST_INVALID", "A non-empty placement request identifier is required."));

        ValidateGeometry(request.Geometry, errors);
        ValidateSelection(request, errors);
        ValidateAxis(request, errors);
        ValidateModule(request.Module, errors);

        return errors;
    }

    private static void ValidateGeometry(GeometrySet? geometry, List<PlacementMessage> errors)
    {
        if (geometry is null)
        {
            errors.Add(Error("PLC_DEPENDENCY_MISSING", "Accepted geometry is required."));
            return;
        }

        if (string.IsNullOrWhiteSpace(geometry.RequestId))
            errors.Add(Error("GEO_REQUEST_ID_REQUIRED", "A geometry request identifier is required."));
        if (string.IsNullOrWhiteSpace(geometry.CoordinateSystemId))
            errors.Add(Error("GEO_COORDINATE_SYSTEM_REQUIRED", "A coordinate-system identifier is required."));
        if (!string.Equals(geometry.LinearUnit, "mm", StringComparison.Ordinal))
            errors.Add(Error("GEO_UNIT_INVALID", "Geometry linear unit must be mm."));
        if (string.IsNullOrWhiteSpace(geometry.RoofId))
            errors.Add(Error("GEO_IDENTIFIER_REQUIRED", "A roof identifier is required."));
        if (geometry.Roof is null)
            errors.Add(Error("GEO_ROOF_REQUIRED", "Exactly one roof polygon is required."));
        if (geometry.Partitions is null || geometry.Partitions.Count == 0)
            errors.Add(Error("GEO_PARTITION_COLLECTION_EMPTY", "At least one partition is required."));

        if (geometry.Roof is null || geometry.Partitions is null)
            return;

        var roofValid = ValidatePolygon(geometry.RoofId, geometry.Roof, errors);
        var identifiers = new HashSet<string>(StringComparer.Ordinal);
        if (!string.IsNullOrWhiteSpace(geometry.RoofId)) identifiers.Add(geometry.RoofId);

        foreach (var partition in geometry.Partitions)
        {
            if (partition is null || string.IsNullOrWhiteSpace(partition.Id))
            {
                errors.Add(Error("GEO_IDENTIFIER_REQUIRED", "Every partition requires an identifier."));
                continue;
            }

            if (!identifiers.Add(partition.Id))
                errors.Add(Error("GEO_IDENTIFIER_DUPLICATE", $"Geometry identifier '{partition.Id}' is duplicated."));

            if (partition.Boundary is null)
            {
                errors.Add(Error("GEO_VERTEX_COUNT_INVALID", $"Partition '{partition.Id}' has no polygon."));
                continue;
            }

            var partitionValid = ValidatePolygon(partition.Id, partition.Boundary, errors);
            if (roofValid && partitionValid && !Geometry2D.PolygonFullyInside(partition.Boundary, geometry.Roof))
                errors.Add(Error("GEO_PARTITION_OUTSIDE_ROOF", $"Partition '{partition.Id}' is not fully contained by the roof."));
        }
    }

    private static bool ValidatePolygon(string identifier, Polygon2D polygon, List<PlacementMessage> errors)
    {
        var valid = true;
        var vertices = polygon.Vertices;
        if (vertices.Any(point => !Geometry2D.IsFinite(point)))
        {
            errors.Add(Error("GEO_COORDINATE_INVALID", $"Geometry '{identifier}' contains a non-finite coordinate."));
            valid = false;
        }

        var distinct = new List<Point2D>();
        foreach (var point in vertices)
            if (distinct.All(existing => !Geometry2D.SamePoint(existing, point))) distinct.Add(point);

        if (distinct.Count < 3)
        {
            errors.Add(Error("GEO_VERTEX_COUNT_INVALID", $"Geometry '{identifier}' requires three distinct vertices."));
            valid = false;
        }

        if (vertices.Count > 0 && Enumerable.Range(0, vertices.Count)
            .Any(index => Geometry2D.SamePoint(vertices[index], vertices[(index + 1) % vertices.Count])))
        {
            errors.Add(Error("GEO_ZERO_LENGTH_EDGE", $"Geometry '{identifier}' contains a zero-length edge."));
            valid = false;
        }

        if (vertices.All(Geometry2D.IsFinite) && Math.Abs(Geometry2D.SignedArea(polygon)) <= Geometry2D.Epsilon)
        {
            errors.Add(Error("GEO_AREA_INVALID", $"Geometry '{identifier}' has zero enclosed area."));
            valid = false;
        }

        if (distinct.Count >= 3 && vertices.All(Geometry2D.IsFinite) && !Geometry2D.IsSimple(polygon))
        {
            errors.Add(Error("GEO_POLYGON_NOT_SIMPLE", $"Geometry '{identifier}' is not a simple polygon."));
            valid = false;
        }

        return valid;
    }

    private static void ValidateSelection(LayoutRequest request, List<PlacementMessage> errors)
    {
        if (request.Geometry is null) return;
        if (string.IsNullOrWhiteSpace(request.SelectedPartitionId))
        {
            errors.Add(Error("SEL_SELECTION_REQUIRED", "Exactly one selected partition identifier is required."));
            return;
        }

        if (request.Geometry.Partitions is null
            || request.Geometry.Partitions.Count(partition => partition?.Id == request.SelectedPartitionId) != 1)
            errors.Add(Error("SEL_PARTITION_UNKNOWN", $"Selected partition '{request.SelectedPartitionId}' is not uniquely present."));
    }

    private static void ValidateAxis(LayoutRequest request, List<PlacementMessage> errors)
    {
        if (request.Axis is null)
        {
            errors.Add(Error("PLC_DEPENDENCY_MISSING", "An Accepted Local Axis is required."));
            return;
        }

        if (string.IsNullOrWhiteSpace(request.Axis.RequestId) || string.IsNullOrWhiteSpace(request.Axis.Id))
            errors.Add(Error("AXS_REQUEST_ID_REQUIRED", "Axis request and Axis identifiers are required."));
        if (!string.Equals(request.Axis.PartitionId, request.SelectedPartitionId, StringComparison.Ordinal))
            errors.Add(Error("AXS_PARTITION_REFERENCE_MISMATCH", "The Local Axis must belong to the selected partition."));
        if (request.Geometry is not null
            && !string.Equals(request.Axis.CoordinateSystemId, request.Geometry.CoordinateSystemId, StringComparison.Ordinal))
            errors.Add(Error("AXS_COORDINATE_SYSTEM_MISMATCH", "Axis and geometry coordinate systems must match."));
        if (!string.Equals(request.Axis.LinearUnit, "mm", StringComparison.Ordinal))
            errors.Add(Error("AXS_UNIT_INVALID", "Axis linear unit must be mm."));
        if (!Geometry2D.IsFinite(request.Axis.Origin))
            errors.Add(Error("AXS_ORIGIN_INVALID", "Axis origin must contain finite coordinates."));
        if (!double.IsFinite(request.Axis.RotationDegrees))
            errors.Add(Error("AXS_ROTATION_INVALID", "Axis rotation must be finite."));
    }

    private static void ValidateModule(ModuleDefinition? module, List<PlacementMessage> errors)
    {
        if (module is null)
        {
            errors.Add(Error("PLC_DEPENDENCY_MISSING", "An Accepted module definition is required."));
            return;
        }

        if (string.IsNullOrWhiteSpace(module.RequestId))
            errors.Add(Error("MOD_REQUEST_ID_REQUIRED", "A module request identifier is required."));
        if (string.IsNullOrWhiteSpace(module.Id))
            errors.Add(Error("MOD_ID_REQUIRED", "A module identifier is required."));
        if (!string.Equals(module.LinearUnit, "mm", StringComparison.Ordinal))
            errors.Add(Error("MOD_LINEAR_UNIT_INVALID", "Module linear unit must be mm."));
        if (!string.Equals(module.PowerUnit, "Wp", StringComparison.Ordinal))
            errors.Add(Error("MOD_POWER_UNIT_INVALID", "Module power unit must be Wp."));
        if (!double.IsFinite(module.PhysicalWidthMm) || module.PhysicalWidthMm <= 0)
            errors.Add(Error("MOD_WIDTH_INVALID", "Module physical width must be finite and positive."));
        if (!double.IsFinite(module.PhysicalLengthMm) || module.PhysicalLengthMm <= 0)
            errors.Add(Error("MOD_LENGTH_INVALID", "Module physical length must be finite and positive."));
        if (!double.IsFinite(module.RatedPowerWp) || module.RatedPowerWp <= 0)
            errors.Add(Error("MOD_RATED_POWER_INVALID", "Module rated power must be finite and positive."));
        if (!Enum.IsDefined(module.Orientation))
            errors.Add(Error("MOD_ORIENTATION_INVALID", "Module orientation is unsupported."));
        if (!double.IsFinite(module.ColumnGapMm) || module.ColumnGapMm < 0)
            errors.Add(Error("MOD_COLUMN_GAP_INVALID", "Column gap must be finite and non-negative."));
        if (!double.IsFinite(module.RowGapMm) || module.RowGapMm < 0)
            errors.Add(Error("MOD_ROW_GAP_INVALID", "Row gap must be finite and non-negative."));
        if (!double.IsFinite(module.EdgeMarginMm) || module.EdgeMarginMm < 0)
            errors.Add(Error("MOD_EDGE_MARGIN_INVALID", "Edge margin must be finite and non-negative."));
    }

    private static IReadOnlyList<PlacementMessage> BuildWarnings(
        string requestId,
        int panelCount,
        int candidateCount,
        IReadOnlyList<RowDecision> rows)
    {
        var warnings = new List<PlacementMessage>();
        if (panelCount == 0)
        {
            warnings.Add(new PlacementMessage("PLC_NO_PANEL_FITS", $"No panel fits placement request '{requestId}'."));
            warnings.Add(new PlacementMessage("PLC_EMPTY_PLACEMENT_RESULT", $"Placement request '{requestId}' has an empty panel collection."));
        }

        if (candidateCount > panelCount)
            warnings.Add(new PlacementMessage("PLC_UNUSED_AREA_REMAINS", "At least one candidate was rejected by partition containment."));

        warnings.AddRange(rows
            .Where(row => row.Accepted > 0 && row.Rejected > 0)
            .Select(row => new PlacementMessage("PLC_PARTIAL_ROW", $"Row {row.Number} contains accepted and rejected candidates.", row.Number)));

        return warnings;
    }

    private static LayoutResult Rejected(LayoutRequest? request, IReadOnlyList<PlacementMessage> errors) =>
        new(
            request?.Id ?? string.Empty,
            request?.SelectedPartitionId,
            PlacementStatus.Rejected,
            [],
            0,
            [],
            errors);

    private static PlacementMessage Error(string code, string message) => new(code, message);

    private sealed class RowDecision(int number)
    {
        public int Number { get; } = number;
        public int Accepted { get; set; }
        public int Rejected { get; set; }
    }
}
