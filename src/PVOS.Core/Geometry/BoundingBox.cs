namespace PVOS.Core.Geometry;

public readonly record struct BoundingBox(Point2D Min, Point2D Max)
{
    public double Width => Max.X - Min.X;

    public double Height => Max.Y - Min.Y;

    public Point2D Center =>
        new((Min.X + Max.X) / 2.0, (Min.Y + Max.Y) / 2.0);

    public bool Contains(Point2D point)
        => point.X >= Min.X &&
           point.X <= Max.X &&
           point.Y >= Min.Y &&
           point.Y <= Max.Y;

    public bool Intersects(BoundingBox other)
        => !(other.Max.X < Min.X ||
             other.Min.X > Max.X ||
             other.Max.Y < Min.Y ||
             other.Min.Y > Max.Y);
}