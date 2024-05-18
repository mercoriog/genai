@echo off

REM Check python is installed.
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [SETUP] Python is not installed. Please install python.
    exit /b 1
) else (
    echo [SETUP] Python is installed.
)

REM Check Python version
for /f "tokens=2 delims= " %%v in ('python --version 2^>^&1') do set "python_version=%%v"

echo %python_version% | findstr "^3\.12\." >nul
if %errorlevel% neq 0 (
    echo [SETUP] Python 3.12.x is not installed. Please install python 3.12, ADD TO YOUR PATH and retry.
    exit /b 1
) else (
    echo [SETUP] Python 3.12.x is installed.
)

REM Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [SETUP] pip is not installed. Please install pip.
    exit /b 1
) else (
    echo [SETUP] pip is installed.
)

REM Set my virtual environment name.
set "virtualenv_name=env"

REM Create virtual environment
python -m venv %virtualenv_name%
if exist env (
    echo [SETUP] Virtual environment created successfully.
) else (
    echo [SETUP] Failed to create virtual environment.
    exit /b 1
)

REM Get setup script abspath.
for /f "delims=" %%A in ("%~f0") do set "script_path=%%~dpA"

REM Get dirname from script abspath.
set "script_dir=%~dp0"

REM Install dependencies.
%script_dir%\env\Scripts\pip install -r %script_dir%requirements.txt
if %errorlevel% neq 0 (
    echo [SETUP] Failed to install required packages. Delete %script_dir%env folder and retry.
    exit /b 1
) else (
    echo [SETUP] Required packages installed successfully.
)

echo [SETUP] Done.

timeout /t 5 >nul