namespace PVOS.Core;

public sealed record LocalAxis(Point2D Origin, double RotationDegrees);

public sealed record Partition(string Id, Polygon2D Boundary, LocalAxis Axis);

public sealed record ModuleSpec(
    double WidthMm,
    double HeightMm,
    double GapXMm,
    double GapYMm,
    double EdgeMarginMm,
    double PowerW);

public sealed record Panel(string Id, IReadOnlyList<Point2D> Corners);

public sealed record LayoutRequest(Partition Partition, ModuleSpec Module);

public sealed record LayoutResult(
    string PartitionId,
    IReadOnlyList<Panel> Panels,
    IReadOnlyList<string> Warnings)
{
    public int PanelCount => Panels.Count;
    public double InstalledKwp(ModuleSpec spec) => PanelCount * spec.PowerW / 1000.0;
}
