using PVOS.Core;
using PVOS.Layout;
using Xunit;

namespace PVOS.Tests;

public sealed class LayoutEngineTests
{
    [Fact]
    public void Generate_Demo001_ReturnsExpectedDeterministicResult()
    {
        var engine = new LayoutEngine();
        var request = CreateRequest();

        var first = engine.Generate(request);
        var second = engine.Generate(request);

        Assert.Equal(PlacementStatus.Accepted, first.Status);
        Assert.Equal(10, first.PanelCount);
        Assert.Equal(5.0, first.InstalledCapacityKwp, 10);
        Assert.Empty(first.Warnings);
        Assert.Empty(first.Errors);
        Assert.Equal(Signature(first), Signature(second));
    }

    [Fact]
    public void Generate_AssignsStableOrderAndGlobalCornerOrder()
    {
        var result = new LayoutEngine().Generate(CreateRequest());
        var first = result.Panels[0];

        Assert.Equal("PNL-000001", first.Id);
        Assert.Equal(1, first.PlacementOrder);
        Assert.Equal(1, first.CandidateIndex);
        Assert.Equal(1, first.Row);
        Assert.Equal(1, first.Column);
        Assert.Equal(
        [
            new Point2D(200, 200),
            new Point2D(1_200, 200),
            new Point2D(1_200, 1_700),
            new Point2D(200, 1_700)
        ], first.Corners);

        Assert.Equal(
            Enumerable.Range(1, result.PanelCount).Select(index => $"PNL-{index:000000}"),
            result.Panels.Select(panel => panel.Id));
    }

    [Fact]
    public void Generate_UsesExplicitModuleOrientation()
    {
        var request = CreateRequest();
        var rotatedModule = request.Module with { Orientation = ModuleOrientation.LengthAlongLocalX };

        var result = new LayoutEngine().Generate(request with { Id = "LAYOUT-REQ-002", Module = rotatedModule });

        Assert.Equal(PlacementStatus.Accepted, result.Status);
        var first = result.Panels[0].Corners;
        Assert.Equal(1_500, first[1].X - first[0].X, 10);
        Assert.Equal(1_000, first[2].Y - first[1].Y, 10);
    }

    [Fact]
    public void Generate_RotatedAxis_IsRepeatableAndReturnsContainedGlobalGeometry()
    {
        var request = CreateRequest();
        var rotated = request with
        {
            Id = "LAYOUT-REQ-ROTATED",
            Axis = request.Axis with { RotationDegrees = 15 }
        };
        var engine = new LayoutEngine();

        var first = engine.Generate(rotated);
        var second = engine.Generate(rotated);

        Assert.Equal(PlacementStatus.Accepted, first.Status);
        Assert.Equal(Signature(first), Signature(second));
        Assert.All(first.Panels, panel =>
            Assert.True(Geometry2D.PolygonFullyInside(new Polygon2D(panel.Corners), request.Geometry.Roof)));
    }

    [Fact]
    public void Generate_NoFit_ReturnsAcceptedEmptyResultAndRequiredWarnings()
    {
        var request = CreateRequest();
        var tooLarge = request.Module with { PhysicalWidthMm = 10_000, PhysicalLengthMm = 10_000 };

        var result = new LayoutEngine().Generate(request with { Id = "LAYOUT-REQ-NOFIT", Module = tooLarge });

        Assert.Equal(PlacementStatus.Accepted, result.Status);
        Assert.Empty(result.Panels);
        Assert.Equal(0, result.PanelCount);
        Assert.Equal(0, result.InstalledCapacityKwp);
        Assert.Equal(
            ["PLC_NO_PANEL_FITS", "PLC_EMPTY_PLACEMENT_RESULT"],
            result.Warnings.Select(warning => warning.Code));
    }

    [Fact]
    public void Generate_ConcavePartition_RejectsCrossingCandidatesAndWarnsPartialRow()
    {
        var boundary = new Polygon2D(
        [
            new Point2D(0, 0),
            new Point2D(3_000, 0),
            new Point2D(3_000, 2_000),
            new Point2D(2_000, 2_000),
            new Point2D(2_000, 1_000),
            new Point2D(1_000, 1_000),
            new Point2D(1_000, 2_000),
            new Point2D(0, 2_000)
        ]);
        var request = CreateRequest(boundary, new ModuleDefinition(
            "MOD-REQ-002", "MOD-002", 900, 900, 400,
            ModuleOrientation.WidthAlongLocalX, 100, 100, 0));

        var result = new LayoutEngine().Generate(request with { Id = "LAYOUT-REQ-CONCAVE" });

        Assert.Equal(PlacementStatus.Accepted, result.Status);
        Assert.Equal(5, result.PanelCount);
        Assert.Contains(result.Warnings, warning => warning.Code == "PLC_UNUSED_AREA_REMAINS");
        Assert.Contains(result.Warnings, warning => warning.Code == "PLC_PARTIAL_ROW" && warning.Row == 2);
        Assert.All(result.Panels, panel =>
            Assert.True(Geometry2D.PolygonFullyInside(new Polygon2D(panel.Corners), boundary)));
    }

    [Fact]
    public void Generate_BoundaryContact_IsAccepted()
    {
        var boundary = Rectangle(2_000, 1_000);
        var module = new ModuleDefinition(
            "MOD-REQ-003", "MOD-003", 1_000, 1_000, 500,
            ModuleOrientation.WidthAlongLocalX, 0, 0, 0);

        var result = new LayoutEngine().Generate(CreateRequest(boundary, module));

        Assert.Equal(2, result.PanelCount);
        Assert.Empty(result.Warnings);
    }

    [Fact]
    public void Generate_InvalidGeometry_ReturnsStableRejectedResult()
    {
        var bowTie = new Polygon2D(
        [
            new Point2D(0, 0),
            new Point2D(2_000, 2_000),
            new Point2D(0, 2_000),
            new Point2D(2_000, 0)
        ]);
        var request = CreateRequest(bowTie);

        var result = new LayoutEngine().Generate(request);

        Assert.Equal(PlacementStatus.Rejected, result.Status);
        Assert.Empty(result.Panels);
        Assert.Equal(0, result.InstalledCapacityKwp);
        Assert.Contains(result.Errors, error => error.Code == "GEO_AREA_INVALID");
        Assert.Contains(result.Errors, error => error.Code == "GEO_POLYGON_NOT_SIMPLE");
    }

    [Fact]
    public void Generate_UnknownSelection_ReturnsRejectedWithoutFallback()
    {
        var request = CreateRequest() with { SelectedPartitionId = "UNKNOWN" };

        var result = new LayoutEngine().Generate(request);

        Assert.Equal(PlacementStatus.Rejected, result.Status);
        Assert.Contains(result.Errors, error => error.Code == "SEL_PARTITION_UNKNOWN");
        Assert.Contains(result.Errors, error => error.Code == "AXS_PARTITION_REFERENCE_MISMATCH");
    }

    [Fact]
    public void Generate_InvalidAxisAndModule_ReturnsSpecificationCodes()
    {
        var request = CreateRequest();
        var invalid = request with
        {
            Axis = request.Axis with { RotationDegrees = double.NaN },
            Module = request.Module with { PhysicalWidthMm = 0, ColumnGapMm = -1 }
        };

        var result = new LayoutEngine().Generate(invalid);

        Assert.Equal(PlacementStatus.Rejected, result.Status);
        Assert.Contains(result.Errors, error => error.Code == "AXS_ROTATION_INVALID");
        Assert.Contains(result.Errors, error => error.Code == "MOD_WIDTH_INVALID");
        Assert.Contains(result.Errors, error => error.Code == "MOD_COLUMN_GAP_INVALID");
    }

    [Fact]
    public void AxisTransform_RoundTripMeetsApprovedTolerance()
    {
        var axis = CreateRequest().Axis with { RotationDegrees = 37.5 };
        var transform = new AxisTransform(axis);
        var source = new Point2D(12_345.678, -9_876.543);

        var roundTrip = transform.ToGlobal(transform.ToLocal(source));
        var distance = Math.Sqrt(Math.Pow(roundTrip.X - source.X, 2) + Math.Pow(roundTrip.Y - source.Y, 2));

        Assert.True(distance <= 1e-6);
    }

    private static LayoutRequest CreateRequest(Polygon2D? boundary = null, ModuleDefinition? module = null)
    {
        boundary ??= Rectangle(6_000, 4_000);
        var partition = new Partition("PART-001", boundary);
        var geometry = new GeometrySet(
            "GEO-REQ-001", "GEO-SET-001", "ROOF-001", boundary, [partition]);
        var axis = new LocalAxis(
            "AXS-REQ-001", "AXS-001", partition.Id, new Point2D(0, 0), 0);
        module ??= new ModuleDefinition(
            "MOD-REQ-001", "MOD-001", 1_000, 1_500, 500,
            ModuleOrientation.WidthAlongLocalX, 100, 100, 200);
        return new LayoutRequest("LAYOUT-REQ-001", geometry, partition.Id, axis, module);
    }

    private static Polygon2D Rectangle(double width, double height) => new(
    [
        new Point2D(0, 0),
        new Point2D(width, 0),
        new Point2D(width, height),
        new Point2D(0, height)
    ]);

    private static string Signature(LayoutResult result) => string.Join("|",
        result.Status,
        result.PanelCount,
        result.InstalledCapacityKwp,
        string.Join(";", result.Panels.Select(panel =>
            $"{panel.Id}:{panel.PlacementOrder}:{panel.CandidateIndex}:{panel.Row}:{panel.Column}:" +
            string.Join(",", panel.Corners.Select(point => $"{point.X:R}/{point.Y:R}")))),
        string.Join(";", result.Warnings.Select(warning => $"{warning.Code}:{warning.Row}")),
        string.Join(";", result.Errors.Select(error => error.Code)));
}
