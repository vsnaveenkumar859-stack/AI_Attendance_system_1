@echo off
title AI Attendance System
echo ========================================================
echo          Starting AI Attendance System
echo ========================================================
cd /d "%~dp0"

if exist "venv\Scripts\python.exe" (
    echo Activating virtual environment...
    venv\Scripts\python.exe run.py
) else (
    echo Virtual environment not found. Using system Python...
    python run.py
)

pause
