using PVOS.Core;
using Xunit;

namespace PVOS.Tests;

public sealed class GeometryTests
{
    private static readonly Polygon2D Square = new(
    [
        new Point2D(0, 0),
        new Point2D(100, 0),
        new Point2D(100, 100),
        new Point2D(0, 100)
    ]);

    [Fact]
    public void PointInPolygon_IncludesInteriorAndBoundary()
    {
        Assert.True(Geometry2D.PointInPolygon(new Point2D(50, 50), Square));
        Assert.True(Geometry2D.PointInPolygon(new Point2D(0, 50), Square));
        Assert.False(Geometry2D.PointInPolygon(new Point2D(150, 50), Square));
    }

    [Fact]
    public void PolygonFullyInside_RejectsEdgeCrossingConcaveBoundary()
    {
        var concave = new Polygon2D(
        [
            new Point2D(0, 0),
            new Point2D(100, 0),
            new Point2D(100, 100),
            new Point2D(60, 100),
            new Point2D(60, 40),
            new Point2D(40, 40),
            new Point2D(40, 100),
            new Point2D(0, 100)
        ]);
        var crossing = new Polygon2D(
        [
            new Point2D(20, 20),
            new Point2D(80, 20),
            new Point2D(80, 80),
            new Point2D(20, 80)
        ]);

        Assert.False(Geometry2D.PolygonFullyInside(crossing, concave));
    }

    [Fact]
    public void IsSimple_RejectsSelfIntersection()
    {
        var bowTie = new Polygon2D(
        [
            new Point2D(0, 0),
            new Point2D(100, 100),
            new Point2D(0, 100),
            new Point2D(100, 0)
        ]);

        Assert.False(Geometry2D.IsSimple(bowTie));
    }
}
