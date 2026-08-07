using System.Text.Json;
using PVOS.Core;
using Xunit;

namespace PVOS.Tests;

public sealed class CandidateAIntegrityTests
{
    private static readonly string RepositoryRoot = Path.GetFullPath(Path.Combine(
        AppContext.BaseDirectory, "..", "..", "..", "..", ".."));

    [Fact]
    public void CoreInvariantInventory_IsOwnedUniqueAndTraceable()
    {
        using var document = Load("PRODUCT/integrity/core-invariants-v1.json");
        var root = document.RootElement;
        Assert.Equal("C# Mainline Product Owner", root.GetProperty("owner").GetString());
        var invariants = root.GetProperty("invariants").EnumerateArray().ToArray();
        Assert.NotEmpty(invariants);
        Assert.Equal(invariants.Length, invariants.Select(item => item.GetProperty("id").GetString()).Distinct().Count());
        foreach (var invariant in invariants)
        {
            Assert.False(string.IsNullOrWhiteSpace(invariant.GetProperty("claim").GetString()));
            Assert.True(File.Exists(Absolute(invariant.GetProperty("source").GetString()!)));
            Assert.False(string.IsNullOrWhiteSpace(invariant.GetProperty("verification").GetString()));
        }
    }

    [Fact]
    public void FailureContract_ClassifiesEveryExposedDiagnosticCategory()
    {
        using var document = Load("PRODUCT/integrity/failure-contract-v1.json");
        var root = document.RootElement;
        Assert.False(root.GetProperty("unknown_items_allowed").GetBoolean());
        var items = root.GetProperty("items").EnumerateArray().ToArray();
        Assert.Contains(items, item => item.GetProperty("item").GetString()!.Contains("Code"));
        Assert.Contains(items, item => item.GetProperty("item").GetString()!.Contains("Message"));
        Assert.Contains(items, item => item.GetProperty("item").GetString() == "ordering");
        Assert.Contains(items, item => item.GetProperty("item").GetString()!.Contains("Row"));
        Assert.All(items, item => Assert.Contains(item.GetProperty("class").GetString(), new[] { "A", "B", "C" }));
    }

    [Fact]
    public void Phase1Lineage_CoversResultAndPreservesExclusions()
    {
        using var document = Load("PRODUCT/integrity/result-lineage-phase1-v1.json");
        var root = document.RootElement;
        Assert.Equal(new[] { "Input Identity", "C# Product Version Identity", "Execution Identity", "Result Identity", "Evidence Reference" },
            root.GetProperty("flow").EnumerateArray().Select(item => item.GetString()));
        var registeredFields = root.GetProperty("result_fields").EnumerateArray().Select(item => item.GetString()!).ToHashSet();
        var actualFields = typeof(LayoutResult).GetProperties().Select(property => property.Name).ToHashSet();
        Assert.True(actualFields.SetEquals(registeredFields));
        Assert.Equal(6, root.GetProperty("excluded").GetArrayLength());
    }

    [Fact]
    public void GoldenClaimMapping_CoversManifestAndPersistsPmAdmissions()
    {
        using var mapping = Load("VALIDATION/golden-claim-mapping-v1.json");
        using var manifest = Load("VALIDATION/golden-dataset-v1.json");
        var mapped = mapping.RootElement.GetProperty("scenarios").EnumerateArray().ToDictionary(
            item => item.GetProperty("id").GetString()!, item => item.GetProperty("admission").GetString()!);
        var manifested = manifest.RootElement.GetProperty("scenarios").EnumerateArray()
            .Select(item => item.GetProperty("scenario_id").GetString()!).ToHashSet();
        Assert.True(manifested.SetEquals(mapped.Keys));
        foreach (var id in Enumerable.Range(4, 5).Select(number => $"PVOS-GOLDEN-{number:000}"))
            Assert.Equal("PM_APPROVED_PERSISTED", mapped[id]);
        Assert.True(File.Exists(Absolute(mapping.RootElement.GetProperty("admission_record").GetString()!)));
        Assert.True(File.Exists(Absolute(mapping.RootElement.GetProperty("contradiction_policy").GetString()!)));
    }

    private static JsonDocument Load(string relativePath) =>
        JsonDocument.Parse(File.ReadAllText(Absolute(relativePath)));

    private static string Absolute(string relativePath) => Path.Combine(
        RepositoryRoot, relativePath.Replace('/', Path.DirectorySeparatorChar));
}
