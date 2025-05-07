@echo off
REM Run script for Windows

set MINICONDA_DIR=%CD%\miniconda3
set ENV_NAME=youpuller_env

echo Uruchamianie aplikacji na Windows...

REM Initialize conda
call "%MINICONDA_DIR%\Scripts\activate.bat"

REM Activate environment
call conda activate %MINICONDA_DIR%\envs\%ENV_NAME%

REM Run the Flask app
python frontend\app.py
