using PVOS.Core;

namespace PVOS.Layout;

public sealed class LayoutEngine
{
    public LayoutResult Generate(LayoutRequest request)
    {
        Validate(request.Module);

        var transform = new AxisTransform(request.Partition.Axis);
        var localBoundary = transform.ToLocal(request.Partition.Boundary);
        var bbox = Geometry2D.BoundingBox(localBoundary);
        var spec = request.Module;

        var minX = bbox.MinX + spec.EdgeMarginMm;
        var minY = bbox.MinY + spec.EdgeMarginMm;
        var maxX = bbox.MaxX - spec.EdgeMarginMm;
        var maxY = bbox.MaxY - spec.EdgeMarginMm;
        var pitchX = spec.WidthMm + spec.GapXMm;
        var pitchY = spec.HeightMm + spec.GapYMm;

        var panels = new List<Panel>();
        var id = 1;

        for (var y = minY; y + spec.HeightMm <= maxY + 1e-9; y += pitchY)
        {
            for (var x = minX; x + spec.WidthMm <= maxX + 1e-9; x += pitchX)
            {
                var candidate = new Rect2D(x, y, x + spec.WidthMm, y + spec.HeightMm);
                if (!Geometry2D.RectangleFullyInside(candidate, localBoundary))
                    continue;

                var globalCorners = candidate.Corners.Select(transform.ToGlobal).ToArray();
                panels.Add(new Panel($"P{id++:0000}", globalCorners));
            }
        }

        var warnings = panels.Count == 0
            ? new[] { "No panels fit inside this partition with the current module and margin settings." }
            : Array.Empty<string>();

        return new LayoutResult(request.Partition.Id, panels, warnings);
    }

    private static void Validate(ModuleSpec spec)
    {
        if (spec.WidthMm <= 0 || spec.HeightMm <= 0)
            throw new ArgumentOutOfRangeException(nameof(spec), "Module dimensions must be positive.");
        if (spec.GapXMm < 0 || spec.GapYMm < 0 || spec.EdgeMarginMm < 0)
            throw new ArgumentOutOfRangeException(nameof(spec), "Gap and margin values cannot be negative.");
    }
}
