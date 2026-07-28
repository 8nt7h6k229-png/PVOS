using PVOS.Core;
using PVOS.Layout;

var roof = new Polygon2D(
[
    new Point2D(0, 0),
    new Point2D(20_000, 0),
    new Point2D(20_000, 10_000),
    new Point2D(0, 10_000)
]);

var partition = new Partition(
    Id: "PART-001",
    Boundary: roof,
    Axis: new LocalAxis(new Point2D(0, 0), RotationDegrees: 15));

var module = new ModuleSpec(
    WidthMm: 1_133,
    HeightMm: 1_907,
    GapXMm: 10,
    GapYMm: 20,
    EdgeMarginMm: 300,
    PowerW: 550);

var result = new LayoutEngine().Generate(new LayoutRequest(partition, module));

Console.WriteLine("PVOS independent layout run");
Console.WriteLine($"Partition : {result.PartitionId}");
Console.WriteLine($"Axis      : {partition.Axis.RotationDegrees:F1} deg");
Console.WriteLine($"Panels    : {result.PanelCount}");
Console.WriteLine($"Capacity  : {result.InstalledKwp(module):F3} kWp");

foreach (var warning in result.Warnings)
    Console.WriteLine($"Warning   : {warning}");
