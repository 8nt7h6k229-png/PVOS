namespace PVOS.Core;

public static class Geometry2D
{
    public const double Epsilon = 1e-9;

    public static bool IsFinite(Point2D point) =>
        double.IsFinite(point.X) && double.IsFinite(point.Y);

    public static bool SamePoint(Point2D a, Point2D b) =>
        Math.Abs(a.X - b.X) <= Epsilon && Math.Abs(a.Y - b.Y) <= Epsilon;

    public static Rect2D BoundingBox(Polygon2D polygon)
    {
        if (polygon.Vertices.Count == 0)
            throw new ArgumentException("A bounding box requires at least one point.", nameof(polygon));

        return new Rect2D(
            polygon.Vertices.Min(point => point.X),
            polygon.Vertices.Min(point => point.Y),
            polygon.Vertices.Max(point => point.X),
            polygon.Vertices.Max(point => point.Y));
    }

    public static double SignedArea(Polygon2D polygon)
    {
        var twiceArea = 0.0;
        for (var i = 0; i < polygon.Vertices.Count; i++)
        {
            var a = polygon.Vertices[i];
            var b = polygon.Vertices[(i + 1) % polygon.Vertices.Count];
            twiceArea += a.X * b.Y - b.X * a.Y;
        }

        return twiceArea / 2.0;
    }

    public static bool IsSimple(Polygon2D polygon)
    {
        var count = polygon.Vertices.Count;
        if (count < 3) return false;

        for (var i = 0; i < count; i++)
        {
            var a1 = polygon.Vertices[i];
            var a2 = polygon.Vertices[(i + 1) % count];

            for (var j = i + 1; j < count; j++)
            {
                if (j == i || j == (i + 1) % count || (j + 1) % count == i)
                    continue;

                var b1 = polygon.Vertices[j];
                var b2 = polygon.Vertices[(j + 1) % count];
                if (SegmentsIntersect(a1, a2, b1, b2))
                    return false;
            }
        }

        return true;
    }

    public static bool PointInPolygon(Point2D point, Polygon2D polygon, bool includeBoundary = true)
    {
        if (polygon.Vertices.Count < 3) return false;

        var inside = false;
        var vertices = polygon.Vertices;

        for (var i = 0; i < vertices.Count; i++)
        {
            var a = vertices[i];
            var b = vertices[(i + 1) % vertices.Count];

            if (PointOnSegment(point, a, b))
                return includeBoundary;

            var crosses = (a.Y > point.Y) != (b.Y > point.Y);
            if (!crosses) continue;

            var xAtY = (b.X - a.X) * (point.Y - a.Y) / (b.Y - a.Y) + a.X;
            if (point.X < xAtY)
                inside = !inside;
        }

        return inside;
    }

    public static bool PolygonFullyInside(Polygon2D subject, Polygon2D container)
    {
        if (subject.Vertices.Count < 3 || container.Vertices.Count < 3)
            return false;

        if (subject.Vertices.Any(point => !PointInPolygon(point, container)))
            return false;

        for (var i = 0; i < subject.Vertices.Count; i++)
        {
            var a = subject.Vertices[i];
            var b = subject.Vertices[(i + 1) % subject.Vertices.Count];

            for (var j = 0; j < container.Vertices.Count; j++)
            {
                var c = container.Vertices[j];
                var d = container.Vertices[(j + 1) % container.Vertices.Count];
                if (SegmentsProperlyIntersect(a, b, c, d))
                    return false;
            }

            var midpoint = new Point2D((a.X + b.X) / 2.0, (a.Y + b.Y) / 2.0);
            if (!PointInPolygon(midpoint, container))
                return false;
        }

        return true;
    }

    public static bool RectangleFullyInside(Rect2D rectangle, Polygon2D polygon) =>
        PolygonFullyInside(new Polygon2D(rectangle.Corners), polygon);

    private static bool SegmentsIntersect(Point2D a, Point2D b, Point2D c, Point2D d)
    {
        var o1 = Orientation(a, b, c);
        var o2 = Orientation(a, b, d);
        var o3 = Orientation(c, d, a);
        var o4 = Orientation(c, d, b);

        if (o1 * o2 < 0 && o3 * o4 < 0) return true;
        return o1 == 0 && PointOnSegment(c, a, b)
            || o2 == 0 && PointOnSegment(d, a, b)
            || o3 == 0 && PointOnSegment(a, c, d)
            || o4 == 0 && PointOnSegment(b, c, d);
    }

    private static bool SegmentsProperlyIntersect(Point2D a, Point2D b, Point2D c, Point2D d)
    {
        var o1 = Orientation(a, b, c);
        var o2 = Orientation(a, b, d);
        var o3 = Orientation(c, d, a);
        var o4 = Orientation(c, d, b);
        return o1 * o2 < 0 && o3 * o4 < 0;
    }

    private static int Orientation(Point2D a, Point2D b, Point2D c)
    {
        var cross = (b.X - a.X) * (c.Y - a.Y) - (b.Y - a.Y) * (c.X - a.X);
        return Math.Abs(cross) <= Epsilon ? 0 : Math.Sign(cross);
    }

    private static bool PointOnSegment(Point2D point, Point2D a, Point2D b)
    {
        if (Orientation(a, b, point) != 0) return false;

        return point.X >= Math.Min(a.X, b.X) - Epsilon
            && point.X <= Math.Max(a.X, b.X) + Epsilon
            && point.Y >= Math.Min(a.Y, b.Y) - Epsilon
            && point.Y <= Math.Max(a.Y, b.Y) + Epsilon;
    }
}
