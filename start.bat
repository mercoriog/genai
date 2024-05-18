@echo off
REM Get setup script abspath.
for /f "delims=" %%A in ("%~f0") do set "script_path=%%~dpA"

REM Get dirname from script abspath.
set "script_dir=%~dp0"

REM Set my virtual environment name.
set "virtualenv_name=env"

REM Set correct directory where to store 'genaienv'.
set "venv_path=%script_dir%%virtualenv_name%"

REM Activate virtual environment.
echo [START] Start 'genai.py'...
%venv_path%\Scripts\python %script_dir%src\main.py


