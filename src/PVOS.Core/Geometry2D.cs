namespace PVOS.Core;

public static class Geometry2D
{
    private const double Epsilon = 1e-9;

    public static Rect2D BoundingBox(Polygon2D polygon)
    {
        var xs = polygon.Vertices.Select(p => p.X);
        var ys = polygon.Vertices.Select(p => p.Y);
        return new Rect2D(xs.Min(), ys.Min(), xs.Max(), ys.Max());
    }

    public static bool PointInPolygon(Point2D point, Polygon2D polygon, bool includeBoundary = true)
    {
        var inside = false;
        var vertices = polygon.Vertices;

        for (var i = 0; i < vertices.Count; i++)
        {
            var a = vertices[i];
            var b = vertices[(i + 1) % vertices.Count];

            if (includeBoundary && PointOnSegment(point, a, b))
                return true;

            var crosses = (a.Y > point.Y) != (b.Y > point.Y);
            if (!crosses) continue;

            var xAtY = (b.X - a.X) * (point.Y - a.Y) / (b.Y - a.Y) + a.X;
            if (point.X < xAtY)
                inside = !inside;
        }

        return inside;
    }

    public static bool RectangleFullyInside(Rect2D rectangle, Polygon2D polygon) =>
        rectangle.Corners.All(p => PointInPolygon(p, polygon));

    private static bool PointOnSegment(Point2D p, Point2D a, Point2D b)
    {
        var cross = (p.Y - a.Y) * (b.X - a.X) - (p.X - a.X) * (b.Y - a.Y);
        if (Math.Abs(cross) > Epsilon) return false;

        var dot = (p.X - a.X) * (b.X - a.X) + (p.Y - a.Y) * (b.Y - a.Y);
        if (dot < -Epsilon) return false;

        var lengthSquared = Math.Pow(b.X - a.X, 2) + Math.Pow(b.Y - a.Y, 2);
        return dot <= lengthSquared + Epsilon;
    }
}
