using Xunit;
using PVOS.Core;

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
    public void PointInPolygon_Inside_ReturnsTrue() =>
        Assert.True(Geometry2D.PointInPolygon(new Point2D(50, 50), Square));

    [Fact]
    public void PointInPolygon_Outside_ReturnsFalse() =>
        Assert.False(Geometry2D.PointInPolygon(new Point2D(150, 50), Square));
}
