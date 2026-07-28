namespace PVOS.Core;

public readonly record struct Rect2D(double MinX, double MinY, double MaxX, double MaxY)
{
    public double Width => MaxX - MinX;
    public double Height => MaxY - MinY;

    public IReadOnlyList<Point2D> Corners =>
    [
        new(MinX, MinY),
        new(MaxX, MinY),
        new(MaxX, MaxY),
        new(MinX, MaxY)
    ];
}
