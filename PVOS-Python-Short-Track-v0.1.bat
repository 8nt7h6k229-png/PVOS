@echo off
setlocal
cd /d "%~dp0"
if "%~1"=="" (
  echo BLOCKED: Drag a governed project JSON file onto this launcher.
  pause
  exit /b 2
)
py -3 SHORT_TRACK\python\pvos_short_track.py "%~1" --repo "%CD%" --output "%CD%\SHORT_TRACK_OUTPUT"
set "PVOS_EXIT=%ERRORLEVEL%"
echo Reports: %CD%\SHORT_TRACK_OUTPUT
pause
exit /b %PVOS_EXIT%
