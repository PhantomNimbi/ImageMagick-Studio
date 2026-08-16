#!/bin/bash
# ============================================================
#      IMAGEMAGICK STUDIO - AUTOMATED LINUX ENVIRONMENT SETUP
# ============================================================
echo "============================================================"
echo "    IMAGEMAGICK STUDIO - AUTOMATED SYSTEM BOOTSTRAPPER      "
echo "============================================================"
echo ""

# 1. Verify Sudo Privileges
if [ "$EUID" -ne 0 ]; then
    echo "[!] ERROR: This installation script must be run with root privileges (sudo)."
    echo "    Please run: sudo ./setup_linux.sh"
    echo ""
    exit 1
fi

# 2. Detect System Package Manager and Deploy Core Binaries
echo "[*] Checking for system package manager..."
if [ -x "$(command -v apt-get)" ]; then
    echo "[*] Debian/Ubuntu system detected. Updating packages and provisioning dependencies..."
    apt-get update -y
    apt-get install -y python3 python3-pip python3-tk imagemagick
elif [ -x "$(command -v pacman)" ]; then
    echo "[*] Arch Linux system detected. Provisioning dependencies..."
    pacman -Syu --noconfirm python python-pip tk imagemagick
elif [ -x "$(command -v dnf)" ]; then
    echo "[*] Fedora/RHEL system detected. Provisioning dependencies..."
    dnf install -y python3 python3-pip python3-tkinter imagemagick
else
    echo "[!] WARNING: Unsupported Linux distribution package manager."
    echo "    Please ensure python3, python3-pip, python3-tk, and imagemagick are manually installed."
fi

# 3. Synchronize Python Modules via Pip (Run as normal user wrapper)
echo "[*] Installing Python modules via requirements.txt..."
if [ -f "requirements.txt" ]; then
    # Running pip installation securely without root profile footprint leaks
    sudo -u $SUDO_USER python3 -m pip install --upgrade pip --break-system-packages 2>/dev/null || sudo -u $SUDO_USER python3 -m pip install --upgrade pip
    sudo -u $SUDO_USER python3 -m pip install -r requirements.txt --break-system-packages 2>/dev/null || sudo -u $SUDO_USER python3 -m pip install -r requirements.txt
else
    echo "[!] WARNING: requirements.txt not found. Installing default fallbacks..."
    sudo -u $SUDO_USER python3 -m pip install customtkinter pillow --break-system-packages 2>/dev/null || sudo -u $SUDO_USER python3 -m pip install customtkinter pillow
fi

# 4. Compile Optional Asset Layers
if [ -f "make_icon.py" ]; then
    echo "[*] Compiling high-resolution icon graphics..."
    sudo -u $SUDO_USER python3 make_icon.py
fi

echo ""
echo "============================================================"
echo "[SUCCESS]: Linux development workspace setup is complete!"
echo "           Launch the app by calling: python3 main.py"
echo "============================================================"
echo ""
