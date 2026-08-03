namespace PVOS.Core;

public sealed class Polygon2D
{
    public Polygon2D(IEnumerable<Point2D>? vertices)
    {
        Vertices = vertices?.ToArray() ?? [];
    }

    public IReadOnlyList<Point2D> Vertices { get; }
}
