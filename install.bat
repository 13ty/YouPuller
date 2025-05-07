@echo off
REM Install script for Windows

set MINICONDA_DIR=%CD%\miniconda3
set ENV_NAME=youpuller_env

echo Starting installation for Windows...

REM Check if Miniconda is installed
if not exist "%MINICONDA_DIR%" (
    echo Downloading Miniconda installer...
    powershell -Command "Invoke-WebRequest -Uri https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -OutFile miniconda.exe"
    echo Installing Miniconda locally...
    start /wait "" miniconda.exe /InstallationType=JustMe /AddToPath=0 /RegisterPython=0 /S /D=%MINICONDA_DIR%
    del miniconda.exe
) else (
    echo Miniconda already installed.
)

REM Initialize conda
call "%MINICONDA_DIR%\Scripts\activate.bat"

REM Create environment if it doesn't exist
conda info --envs | findstr /R /C:"%ENV_NAME%" >nul
if %errorlevel%==0 (
    echo Conda environment %ENV_NAME% already exists.
) else (
    echo Creating conda environment %ENV_NAME%...
    conda create -y -p %MINICONDA_DIR%\envs\%ENV_NAME% python=3.9
)

REM Activate environment
call conda activate %MINICONDA_DIR%\envs\%ENV_NAME%

REM Install required packages
echo Installing required packages...
pip install --upgrade pip
pip install -r requirements.txt

echo Installation complete. To activate the environment, run:
echo call "%MINICONDA_DIR%\Scripts\activate.bat"
echo conda activate %MINICONDA_DIR%\envs\%ENV_NAME%
