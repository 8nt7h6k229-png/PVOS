namespace PVOS.Core.Geometry;

public readonly record struct Point2D(double X, double Y)
{
    public double DistanceTo(Point2D other)
    {
        var dx = other.X - X;
        var dy = other.Y - Y;

        return Math.Sqrt(dx * dx + dy * dy);
    }

    public static Point2D operator +(Point2D point, Vector2D vector)
        => new(point.X + vector.X, point.Y + vector.Y);

    public static Vector2D operator -(Point2D a, Point2D b)
        => new(a.X - b.X, a.Y - b.Y);
}