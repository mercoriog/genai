@echo off

where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [SETUP] Python is not installed. Please install python.
    exit /b 1
) else (
    echo [SETUP] Python is installed.
)

REM Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [SETUP] pip is not installed. Please install pip.
    exit /b 1
) else (
    echo [SETUP] pip is installed.
)

REM Install gdown library
pip install gdown

REM Check if gdown is installed successfully
pip show gdown >nul 2>&1
if %errorlevel% neq 0 (
    echo [SETUP] gdown installation failed. Please retry.
    exit /b 1
) else (
    echo [SETUP] gdown installed successfully.
)

REM Get setup.sh abspath.
for /f "delims=" %%A in ("%~f0") do set "script_path=%%~dpA"

REM Start src\setup.py python script.
python %script_path%src\setup.py

echo [SETUP] Done.

timeout /t 5 >nul