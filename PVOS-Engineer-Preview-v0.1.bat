@echo off
setlocal
cd /d "%~dp0"
set "PREVIEW_OUTPUT=%~dp0ENGINEER_PREVIEW_OUTPUT"

where py >nul 2>nul
if %errorlevel%==0 (
  set "PYTHON_CMD=py -3"
) else (
  where python >nul 2>nul
  if errorlevel 1 (
    echo [BLOCKED] Python 3 was not found on PATH.
    echo Install Python 3.11 or later, then run this launcher again.
    pause
    exit /b 2
  )
  set "PYTHON_CMD=python"
)

echo PVOS Python Engineer Preview v0.1
echo Governed root: %~dp0
echo Evidence output: %PREVIEW_OUTPUT%
echo.
%PYTHON_CMD% "%~dp0VALIDATION\python\engineer_preview.py" --repo-root "%~dp0" --output-dir "%PREVIEW_OUTPUT%" --repeatability-runs 3
set "PREVIEW_EXIT=%errorlevel%"
echo.
if "%PREVIEW_EXIT%"=="0" echo [PASS] Preview validation completed.
if "%PREVIEW_EXIT%"=="1" echo [FAIL] Preview found evidence that does not match the approved baseline.
if "%PREVIEW_EXIT%"=="2" echo [BLOCKED] Preview could not complete. Review the report and prerequisites.
echo Reports: %PREVIEW_OUTPUT%
pause
exit /b %PREVIEW_EXIT%
