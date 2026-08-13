@echo off
setlocal
set "PA_PYTHON=C:\Users\yarin.s\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if not exist "%PA_PYTHON%" set "PA_PYTHON=python"
if "%~1"=="search" goto search
if "%~1"=="update" goto update
if "%~1"=="status" goto status
if "%~1"=="import-koi" goto importkoi
if "%~1"=="recover-koi" goto recoverkoi
echo Usage: pa-docs.cmd search QUERY [options] ^| update [options] ^| status ^| import-koi PATH ^| recover-koi FILE
exit /b 2
:search
shift
"%PA_PYTHON%" "%~dp0scripts\search.py" %*
exit /b %errorlevel%
:update
shift
"%PA_PYTHON%" "%~dp0scripts\ingest.py" %*
exit /b %errorlevel%
:status
"%PA_PYTHON%" "%~dp0scripts\status.py"
exit /b %errorlevel%
:importkoi
shift
"%PA_PYTHON%" "%~dp0scripts\import_koi.py" %*
exit /b %errorlevel%
:recoverkoi
shift
"%PA_PYTHON%" "%~dp0scripts\import_koi_recovery.py" %*
exit /b %errorlevel%
