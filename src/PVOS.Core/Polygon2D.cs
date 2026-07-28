namespace PVOS.Core;

public sealed class Polygon2D
{
    public Polygon2D(IEnumerable<Point2D> vertices)
    {
        Vertices = vertices.ToArray();
        if (Vertices.Count < 3)
            throw new ArgumentException("Polygon requires at least three vertices.", nameof(vertices));
    }

    public IReadOnlyList<Point2D> Vertices { get; }
}
