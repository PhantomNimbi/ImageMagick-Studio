#!/bin/bash
# ============================================================
#      IMAGEMAGICK STUDIO - AUTOMATED MACOS ENVIRONMENT SETUP
# ============================================================
echo "============================================================"
echo "    IMAGEMAGICK STUDIO - AUTOMATED SYSTEM BOOTSTRAPPER      "
echo "============================================================"
echo ""

# 1. Verify Homebrew is Available
echo "[*] Verifying Homebrew installation environment..."
if ! [ -x "$(command -v brew)" ]; then
    echo "[*] Homebrew not detected. Installing Homebrew framework from repository strings..."
    /bin/bash -c "$(curl -fsSL https://githubusercontent.com)"
    
    # Dynamically inject freshly configured homebrew binary environment tracks into this active shell session
    if [ -d "/opt/homebrew/bin" ]; then
        eval "$(/opt/homebrew/bin/brew shellenv)"
    elif [ -d "/usr/local/bin" ]; then
        eval "$(/usr/local/bin/brew shellenv)"
    fi
else
    echo "[✓] Homebrew is already installed on this machine."
fi

# 2. Provision Core Dependencies via Brew Engine
echo "[*] Updating Homebrew formula indexes..."
brew update

echo "[*] Provisioning Python framework and tools..."
brew install python tcl-tk

echo "[*] Provisioning ImageMagick core CLI binary tools..."
brew install imagemagick

# 3. Synchronize Python Modules via Pip
echo "[*] Synchronizing Python library module layers via pip..."
if [ -f "requirements.txt" ]; then
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
else
    echo "[!] WARNING: requirements.txt not found. Installing default fallbacks..."
    python3 -m pip install customtkinter pillow
fi

# 4. Compile Assets
if [ -f "make_icon.py" ]; then
    echo "[*] Generating system brand icon files..."
    python3 make_icon.py
fi

echo ""
echo "============================================================"
echo "[SUCCESS]: macOS development workspace setup is complete!"
echo "           Launch the app by calling: python3 main.py"
echo "============================================================"
echo ""
