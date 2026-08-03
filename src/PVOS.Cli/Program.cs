using System.Globalization;
using PVOS.Core;
using PVOS.Layout;

var roof = new Polygon2D(
[
    new Point2D(0, 0),
    new Point2D(6_000, 0),
    new Point2D(6_000, 4_000),
    new Point2D(0, 4_000)
]);

var partition = new Partition("PART-001", roof);
var geometry = new GeometrySet(
    "GEO-REQ-001",
    "GEO-SET-001",
    "ROOF-001",
    roof,
    [partition]);
var axis = new LocalAxis(
    "AXS-REQ-001",
    "AXS-001",
    partition.Id,
    new Point2D(0, 0),
    0);
var module = new ModuleDefinition(
    "MOD-REQ-001",
    "MOD-001",
    1_000,
    1_500,
    500,
    ModuleOrientation.WidthAlongLocalX,
    100,
    100,
    200);
var request = new LayoutRequest("LAYOUT-REQ-001", geometry, partition.Id, axis, module);
var result = new LayoutEngine().Generate(request);

Console.WriteLine("Demo-001 Deterministic Placement Engine MVP");
Console.WriteLine($"Request: {result.RequestId}");
Console.WriteLine($"Status: {result.Status}");
Console.WriteLine($"Partition: {result.PartitionId}");
Console.WriteLine($"PanelCount: {result.PanelCount}");
Console.WriteLine($"InstalledCapacityKwp: {result.InstalledCapacityKwp.ToString("F3", CultureInfo.InvariantCulture)}");
Console.WriteLine("PanelGeometry:");

foreach (var panel in result.Panels)
{
    var corners = string.Join("; ", panel.Corners.Select(point =>
        $"({point.X.ToString("F3", CultureInfo.InvariantCulture)},{point.Y.ToString("F3", CultureInfo.InvariantCulture)})"));
    Console.WriteLine($"  {panel.Id} order={panel.PlacementOrder} row={panel.Row} column={panel.Column}: {corners}");
}

Console.WriteLine("PlacementWarnings:");
if (result.Warnings.Count == 0)
    Console.WriteLine("  none");
else
    foreach (var warning in result.Warnings)
        Console.WriteLine($"  {warning.Code}: {warning.Message}");

if (result.Errors.Count > 0)
{
    Console.WriteLine("Errors:");
    foreach (var error in result.Errors)
        Console.WriteLine($"  {error.Code}: {error.Message}");
}
