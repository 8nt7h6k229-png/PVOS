using System.Security.Cryptography;
using System.Text.Json;
using PVOS.Core;
using PVOS.Layout;
using Xunit;

namespace PVOS.Tests;

public sealed class ProductionReadinessRegressionTests
{
    private static readonly string RepositoryRoot = Path.GetFullPath(Path.Combine(
        AppContext.BaseDirectory, "..", "..", "..", "..", ".."));

    [Fact]
    public void Golden007_BoundaryContact_MatchesRuntimeResultAndIsRepeatable()
    {
        using var expected = LoadScenarioOutput("PVOS-GOLDEN-007");
        var boundary = new Polygon2D([new Point2D(0,0), new Point2D(2_000,0), new Point2D(2_000,1_000), new Point2D(0,1_000)]);
        var request = CreateRequest("LAYOUT-REQ-BOUNDARY-CONTACT", new ModuleDefinition(
            "MOD-REQ-007", "MOD-007", 1_000, 1_000, 500, ModuleOrientation.WidthAlongLocalX, 0, 0, 0), boundary);
        var engine = new LayoutEngine();
        var first = engine.Generate(request);
        AssertMatchesExpected(first, expected.RootElement);
        Assert.Equal(Signature(first), Signature(engine.Generate(request)));
    }

    [Fact]
    public void Golden008_InvalidGeometry_MatchesRuntimeResultAndIsRepeatable()
    {
        using var expected = LoadScenarioOutput("PVOS-GOLDEN-008");
        var boundary = new Polygon2D([new Point2D(0,0), new Point2D(2_000,2_000), new Point2D(0,2_000), new Point2D(2_000,0)]);
        var request = CreateRequest("LAYOUT-REQ-INVALID-GEOMETRY", new ModuleDefinition(
            "MOD-REQ-008", "MOD-008", 1_000, 1_500, 500, ModuleOrientation.WidthAlongLocalX, 100, 100, 200), boundary);
        var engine = new LayoutEngine();
        var first = engine.Generate(request);
        AssertMatchesExpected(first, expected.RootElement);
        Assert.Equal(Signature(first), Signature(engine.Generate(request)));
    }

    [Fact]
    public void Golden004_ExplicitOrientation_MatchesRuntimeResultAndIsRepeatable()
    {
        using var expected = LoadScenarioOutput("PVOS-GOLDEN-004");
        var baseline = CreateRequest("LAYOUT-REQ-ORIENTATION", new ModuleDefinition(
            "MOD-REQ-004", "MOD-004", 1_000, 1_500, 500,
            ModuleOrientation.LengthAlongLocalX, 100, 100, 200));
        var engine = new LayoutEngine();
        var first = engine.Generate(baseline);
        AssertMatchesExpected(first, expected.RootElement);
        Assert.Equal(Signature(first), Signature(engine.Generate(baseline)));
    }

    [Fact]
    public void Golden005_ConcavePartition_MatchesRuntimeResultAndIsRepeatable()
    {
        using var expected = LoadScenarioOutput("PVOS-GOLDEN-005");
        var boundary = new Polygon2D([
            new Point2D(0, 0), new Point2D(3_000, 0), new Point2D(3_000, 2_000),
            new Point2D(2_000, 2_000), new Point2D(2_000, 1_000), new Point2D(1_000, 1_000),
            new Point2D(1_000, 2_000), new Point2D(0, 2_000)]);
        var request = CreateRequest("LAYOUT-REQ-CONCAVE", new ModuleDefinition(
            "MOD-REQ-005", "MOD-005", 900, 900, 400,
            ModuleOrientation.WidthAlongLocalX, 100, 100, 0), boundary);
        var engine = new LayoutEngine();
        var first = engine.Generate(request);
        AssertMatchesExpected(first, expected.RootElement);
        Assert.Equal(Signature(first), Signature(engine.Generate(request)));
    }

    [Fact]
    public void Golden006_UnknownPartition_MatchesRuntimeResultAndIsRepeatable()
    {
        using var expected = LoadScenarioOutput("PVOS-GOLDEN-006");
        var request = CreateRequest("LAYOUT-REQ-UNKNOWN-PARTITION", new ModuleDefinition(
            "MOD-REQ-006", "MOD-006", 1_000, 1_500, 500,
            ModuleOrientation.WidthAlongLocalX, 100, 100, 200)) with { SelectedPartitionId = "UNKNOWN" };
        var engine = new LayoutEngine();
        var first = engine.Generate(request);
        AssertMatchesExpected(first, expected.RootElement);
        Assert.Equal(Signature(first), Signature(engine.Generate(request)));
    }

    [Fact]
    public void Golden002_NoFit_MatchesRuntimeResultAndIsRepeatable()
    {
        using var expected = LoadScenarioOutput("PVOS-GOLDEN-002");
        var request = CreateRequest(
            "LAYOUT-REQ-NOFIT",
            new ModuleDefinition(
                "MOD-REQ-NOFIT", "MOD-NOFIT", 10_000, 10_000, 500,
                ModuleOrientation.WidthAlongLocalX, 100, 100, 200));
        var engine = new LayoutEngine();

        var first = engine.Generate(request);
        var second = engine.Generate(request);

        AssertMatchesExpected(first, expected.RootElement);
        Assert.Equal(Signature(first), Signature(second));
    }

    [Fact]
    public void Golden003_InvalidModule_MatchesRuntimeResultAndIsRepeatable()
    {
        using var expected = LoadScenarioOutput("PVOS-GOLDEN-003");
        var request = CreateRequest(
            "LAYOUT-REQ-INVALID-MODULE",
            new ModuleDefinition(
                "MOD-REQ-INVALID", "MOD-INVALID", 0, 1_500, 500,
                ModuleOrientation.WidthAlongLocalX, -1, 100, 200));
        var engine = new LayoutEngine();

        var first = engine.Generate(request);
        var second = engine.Generate(request);

        AssertMatchesExpected(first, expected.RootElement);
        Assert.Equal(Signature(first), Signature(second));
    }

    [Fact]
    public void GoldenScenarioSet_RepresentsThreeDistinctTerminalStateFamilies()
    {
        var demo = new LayoutEngine().Generate(CreateRequest(
            "LAYOUT-REQ-001",
            new ModuleDefinition(
                "MOD-REQ-001", "MOD-001", 1_000, 1_500, 500,
                ModuleOrientation.WidthAlongLocalX, 100, 100, 200)));
        var noFit = new LayoutEngine().Generate(CreateRequest(
            "LAYOUT-REQ-NOFIT",
            new ModuleDefinition(
                "MOD-REQ-NOFIT", "MOD-NOFIT", 10_000, 10_000, 500,
                ModuleOrientation.WidthAlongLocalX, 100, 100, 200)));
        var rejected = new LayoutEngine().Generate(CreateRequest(
            "LAYOUT-REQ-INVALID-MODULE",
            new ModuleDefinition(
                "MOD-REQ-INVALID", "MOD-INVALID", 0, 1_500, 500,
                ModuleOrientation.WidthAlongLocalX, -1, 100, 200)));

        Assert.Equal(PlacementStatus.Accepted, demo.Status);
        Assert.NotEmpty(demo.Panels);
        Assert.Empty(demo.Errors);

        Assert.Equal(PlacementStatus.Accepted, noFit.Status);
        Assert.Empty(noFit.Panels);
        Assert.Equal(
            ["PLC_NO_PANEL_FITS", "PLC_EMPTY_PLACEMENT_RESULT"],
            noFit.Warnings.Select(message => message.Code));

        Assert.Equal(PlacementStatus.Rejected, rejected.Status);
        Assert.Empty(rejected.Panels);
        Assert.Equal(
            ["MOD_WIDTH_INVALID", "MOD_COLUMN_GAP_INVALID"],
            rejected.Errors.Select(message => message.Code));
    }

    [Fact]
    public void GoldenManifest_RegistersThreeScenariosAndAllAssetHashesMatch()
    {
        var manifestPath = Path.Combine(RepositoryRoot, "VALIDATION", "golden-dataset-v1.json");
        using var manifest = JsonDocument.Parse(File.ReadAllText(manifestPath));
        var root = manifest.RootElement;

        Assert.Equal("1.3", root.GetProperty("schema_version").GetString());
        Assert.Equal("PVOS-GOLDEN-SET-001", root.GetProperty("scenario_set_id").GetString());
        Assert.Equal(
            ["PVOS-GOLDEN-001", "PVOS-GOLDEN-002", "PVOS-GOLDEN-003", "PVOS-GOLDEN-004", "PVOS-GOLDEN-005", "PVOS-GOLDEN-006", "PVOS-GOLDEN-007", "PVOS-GOLDEN-008"],
            root.GetProperty("scenarios").EnumerateArray()
                .Select(item => item.GetProperty("scenario_id").GetString()));

        foreach (var asset in root.GetProperty("assets").EnumerateArray())
        {
            var relativePath = asset.GetProperty("path").GetString();
            Assert.False(string.IsNullOrWhiteSpace(relativePath));
            var absolutePath = Path.Combine(RepositoryRoot, relativePath!.Replace('/', Path.DirectorySeparatorChar));
            Assert.True(File.Exists(absolutePath), $"Missing Golden asset: {relativePath}");
            var actual = Convert.ToHexString(SHA256.HashData(File.ReadAllBytes(absolutePath)));
            Assert.Equal(asset.GetProperty("sha256").GetString(), actual);
        }
    }

    private static JsonDocument LoadScenarioOutput(string scenarioId) => JsonDocument.Parse(File.ReadAllText(
        Path.Combine(RepositoryRoot, "VALIDATION", "scenarios", scenarioId, "output.json")));

    private static void AssertMatchesExpected(LayoutResult actual, JsonElement expected)
    {
        Assert.Equal(expected.GetProperty("requestId").GetString(), actual.RequestId);
        Assert.Equal(expected.GetProperty("status").GetString(), actual.Status.ToString());
        Assert.Equal(expected.GetProperty("selectedPartitionId").GetString(), actual.PartitionId);
        Assert.Equal(expected.GetProperty("panelCount").GetInt32(), actual.PanelCount);
        Assert.Equal(expected.GetProperty("installedCapacityKwp").GetDouble(), actual.InstalledCapacityKwp, 10);
        Assert.Equal(
            expected.GetProperty("placementWarnings").EnumerateArray()
                .Select(item => item.GetProperty("code").GetString()),
            actual.Warnings.Select(message => message.Code));
        Assert.Equal(
            expected.GetProperty("errors").EnumerateArray()
                .Select(item => item.GetProperty("code").GetString()),
            actual.Errors.Select(message => message.Code));
    }

    private static LayoutRequest CreateRequest(string requestId, ModuleDefinition module, Polygon2D? requestedBoundary = null)
    {
        var boundary = requestedBoundary ?? new Polygon2D(
        [
            new Point2D(0, 0),
            new Point2D(6_000, 0),
            new Point2D(6_000, 4_000),
            new Point2D(0, 4_000)
        ]);
        var partition = new Partition("PART-001", boundary);
        var geometry = new GeometrySet(
            "GEO-REQ-001", "GEO-SET-001", "ROOF-001", boundary, [partition]);
        var axis = new LocalAxis(
            "AXS-REQ-001", "AXS-001", partition.Id, new Point2D(0, 0), 0);
        return new LayoutRequest(requestId, geometry, partition.Id, axis, module);
    }

    private static string Signature(LayoutResult result) => string.Join("|",
        result.Status,
        result.RequestId,
        result.PartitionId,
        result.PanelCount,
        result.InstalledCapacityKwp,
        string.Join(";", result.Panels.Select(panel =>
            $"{panel.Id}:{panel.PlacementOrder}:{panel.CandidateIndex}:{panel.Row}:{panel.Column}:" +
            string.Join(",", panel.Corners.Select(point => $"{point.X:R}/{point.Y:R}")))),
        string.Join(";", result.Warnings.Select(message => $"{message.Code}:{message.Message}:{message.Row}")),
        string.Join(";", result.Errors.Select(message => $"{message.Code}:{message.Message}")));
}
