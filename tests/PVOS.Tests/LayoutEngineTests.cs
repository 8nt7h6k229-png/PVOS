using Xunit;
using PVOS.Core;
using PVOS.Layout;

namespace PVOS.Tests;

public sealed class LayoutEngineTests
{
    [Fact]
    public void Generate_RectangularPartition_ReturnsPanelsInsideBoundary()
    {
        var boundary = new Polygon2D(
        [
            new Point2D(0, 0),
            new Point2D(20_000, 0),
            new Point2D(20_000, 10_000),
            new Point2D(0, 10_000)
        ]);
        var partition = new Partition("P1", boundary, new LocalAxis(new Point2D(0, 0), 0));
        var spec = new ModuleSpec(1_133, 1_907, 10, 20, 300, 550);

        var result = new LayoutEngine().Generate(new LayoutRequest(partition, spec));

        Assert.NotEmpty(result.Panels);
        Assert.All(result.Panels, panel =>
            Assert.All(panel.Corners, corner => Assert.True(Geometry2D.PointInPolygon(corner, boundary))));
    }

    [Fact]
    public void Generate_UsesPartitionSpecificLocalAxis()
    {
        var boundary = new Polygon2D(
        [
            new Point2D(0, 0),
            new Point2D(20_000, 0),
            new Point2D(20_000, 10_000),
            new Point2D(0, 10_000)
        ]);
        var spec = new ModuleSpec(1_133, 1_907, 10, 20, 300, 550);
        var engine = new LayoutEngine();

        var axis0 = engine.Generate(new LayoutRequest(
            new Partition("P0", boundary, new LocalAxis(new Point2D(0, 0), 0)), spec));
        var axis15 = engine.Generate(new LayoutRequest(
            new Partition("P15", boundary, new LocalAxis(new Point2D(0, 0), 15)), spec));

        Assert.NotEqual(axis0.Panels.First().Corners[0], axis15.Panels.First().Corners[0]);
    }
}
