namespace PVOS.Core;

public sealed class AxisTransform
{
    private readonly Point2D _origin;
    private readonly double _cos;
    private readonly double _sin;

    public AxisTransform(LocalAxis axis)
    {
        _origin = axis.Origin;
        var radians = axis.RotationDegrees * Math.PI / 180.0;
        _cos = Math.Cos(radians);
        _sin = Math.Sin(radians);
    }

    public Point2D ToLocal(Point2D global)
    {
        var dx = global.X - _origin.X;
        var dy = global.Y - _origin.Y;
        return new Point2D(dx * _cos + dy * _sin, -dx * _sin + dy * _cos);
    }

    public Point2D ToGlobal(Point2D local) => new(
        _origin.X + local.X * _cos - local.Y * _sin,
        _origin.Y + local.X * _sin + local.Y * _cos);

    public Polygon2D ToLocal(Polygon2D polygon) => new(polygon.Vertices.Select(ToLocal));
}
