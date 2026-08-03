namespace PVOS.Core;

public enum ModuleOrientation
{
    WidthAlongLocalX,
    LengthAlongLocalX
}

public enum PlacementStatus
{
    Rejected,
    Accepted
}

public sealed record GeometrySet(
    string RequestId,
    string Id,
    string RoofId,
    Polygon2D Roof,
    IReadOnlyList<Partition> Partitions,
    string CoordinateSystemId = "GLOBAL",
    string LinearUnit = "mm");

public sealed record Partition(string Id, Polygon2D Boundary);

public sealed record LocalAxis(
    string RequestId,
    string Id,
    string PartitionId,
    Point2D Origin,
    double RotationDegrees,
    string CoordinateSystemId = "GLOBAL",
    string LinearUnit = "mm");

public sealed record ModuleDefinition(
    string RequestId,
    string Id,
    double PhysicalWidthMm,
    double PhysicalLengthMm,
    double RatedPowerWp,
    ModuleOrientation Orientation,
    double ColumnGapMm,
    double RowGapMm,
    double EdgeMarginMm,
    string LinearUnit = "mm",
    string PowerUnit = "Wp")
{
    public double EffectiveWidthMm => Orientation == ModuleOrientation.WidthAlongLocalX
        ? PhysicalWidthMm
        : PhysicalLengthMm;

    public double EffectiveLengthMm => Orientation == ModuleOrientation.WidthAlongLocalX
        ? PhysicalLengthMm
        : PhysicalWidthMm;

    public double ColumnPitchMm => EffectiveWidthMm + ColumnGapMm;
    public double RowPitchMm => EffectiveLengthMm + RowGapMm;
}

public sealed record LayoutRequest(
    string Id,
    GeometrySet Geometry,
    string SelectedPartitionId,
    LocalAxis Axis,
    ModuleDefinition Module);

public sealed record PlacementMessage(string Code, string Message, int? Row = null);

public sealed record Panel(
    string Id,
    int PlacementOrder,
    int CandidateIndex,
    int Row,
    int Column,
    IReadOnlyList<Point2D> Corners);

public sealed record LayoutResult(
    string RequestId,
    string? PartitionId,
    PlacementStatus Status,
    IReadOnlyList<Panel> Panels,
    double InstalledCapacityKwp,
    IReadOnlyList<PlacementMessage> Warnings,
    IReadOnlyList<PlacementMessage> Errors)
{
    public int PanelCount => Panels.Count;
}
