@echo off
setlocal
set "PA_PYTHON=C:\Users\yarin.s\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if not exist "%PA_PYTHON%" set "PA_PYTHON=python"
"%PA_PYTHON%" "%~dp0scripts\pa_docs.py" %*
exit /b %errorlevel%
