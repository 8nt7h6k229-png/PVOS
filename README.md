# PVOS Implementation 002

Independent PV layout core targeting .NET 8.

## Projects

- `PVOS.Core` — domain and geometry primitives
- `PVOS.Layout` — partition-local-axis grid layout
- `PVOS.Cli` — runnable example
- `PVOS.Tests` — xUnit tests

## Build

```powershell
dotnet restore .\PVOS.sln
dotnet build .\PVOS.sln --configuration Release --no-restore
dotnet test .\PVOS.sln --configuration Release --no-build
```

## Visual Studio

Open `PVOS.sln`, then use **Build > Rebuild Solution**. If NuGet packages have not restored, right-click the solution and choose **Restore NuGet Packages**.

## Correction in 002

- Added explicit `using Xunit;` to test sources.
- Marked `PVOS.Tests` as a test project.
- Added complete Visual Studio runner asset metadata.

The sample uses a 20,000 × 10,000 mm rectangular partition with a partition-specific 15° local axis.
