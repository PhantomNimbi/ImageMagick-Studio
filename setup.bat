@echo off
:: ImageMagick Studio - Zero-Dependency Automated Bootstrapper Setup
title ImageMagick Studio Environment Setup
echo ============================================================
echo      IMAGEMAGICK STUDIO - AUTOMATED SYSTEM BOOTSTRAPPER
echo ============================================================
echo.

:: 1. Verify Administrative Privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [!] ERROR: This installation script must be run as an Administrator.
    echo     Please right-click setup.bat and choose 'Run as administrator'.
    echo.
    pause
    exit /b 1
)

:: 2. Deploy Python Runtime Environment via winget
echo [*] Checking for local Python installation...
where python >nul 2>&1
if %errorLevel% neq 0 (
    echo [*] Python not detected. Provisioning Python via winget...
    winget install --id Python.Python.3.12 --silent --accept-package-agreements --accept-source-agreements
    if %errorLevel% neq 0 (
        echo [!] ERROR: Failed to install Python via winget.
        pause
        exit /b 1
    )
    echo [SUCCESS] Python framework installed.
) else (
    echo [✓] Python is already installed on this system.
)

:: 3. Deploy ImageMagick Engine via winget
echo [*] Checking for local ImageMagick installation...
where magick >nul 2>&1
if %errorLevel% neq 0 (
    echo [*] ImageMagick not detected. Provisioning ImageMagick via winget...
    winget install --id ImageMagick.ImageMagick --silent --accept-package-agreements --accept-source-agreements
    if %errorLevel% neq 0 (
        echo [!] WARNING: Failed to install ImageMagick via winget automatically.
        echo     You may need to download it manually from the official website.
    ) else (
        echo [SUCCESS] ImageMagick engine deployed cleanly.
    )
) else (
    echo [✓] ImageMagick core tool binary is already registered to your PATH.
)

:: 4. Force Dynamic Environment Paths Refresh
echo [*] Refreshing active Environment Path variables...
:: This temporarily maps standard user app routes into this session without requiring a machine reboot
set "PATH=%PATH%;%USERPROFILE%\AppData\Local\Microsoft\WindowsApps;%SystemDrive%\Program Files\ImageMagick"

:: 5. Install Python Module Dependencies via requirements.txt Manifest
echo [*] Synchronizing Python library module layers via pip...
if exist "requirements.txt" (
    py -m pip install --upgrade pip
    py -m pip install -r requirements.txt
) else (
    echo [!] WARNING: requirements.txt not found. Installing default fallbacks...
    py -m pip install customtkinter pillow
)

:: 6. Compile Asset Layers
if exist "make_icon.py" (
    echo [*] Generating high-resolution system brand icons...
    py make_icon.py
)

echo.
echo ============================================================
echo [SUCCESS]: ImageMagick Studio development workspace is ready!
echo            You can now boot up the app by calling: py main.py
echo ============================================================
echo.
pause
