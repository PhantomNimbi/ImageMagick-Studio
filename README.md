# 🛠️ ImageMagick Studio

A professional, cross-platform graphical user interface (GUI) for **ImageMagick** built entirely in Python using CustomTkinter. This workspace houses advanced batch automation workflows, visual chromatic kernels, and pixel geometry manipulation suites under a clean, unified split-panel list engine layout.

---

## ✨ Features

* **Geometry & Format Suite:** Fast proportionally scaled down sampling (`-resize`), precise box boundary extractions (`-crop`), and backdrop canvas extensions (`-extent`).
* **Color & Effects Core:** Tailor compression ratios (`-quality`), clean profile metadata arrays (`-strip`), map color profiles (`-colorspace`), and apply localized convolution matrices.
* **Mass Batch Processing Engine:** Automate directory evaluations over hundreds of media files simultaneously using custom extension filters and arguments chain strings.
* **Diagnostics Log Console:** Built-in un-sandboxed raw CLI pipeline simulation field alongside instant full-detail metadata extraction pipelines (`identify -verbose`).

---

## 📁 System Architecture Layout

```text
MagickStudio/
├── main.py                # Main Application Entry Bootloader
├── core.py                # Shared Subprocess Wrapper & Styling Guide
├── requirements.txt       # Python Dependencies Manifest
├── setup.bat              # Windows Automated Bootstrapper Installer
├── setup_linux.sh         # Linux Automated Bootstrapper Installer
├── setup_mac.sh           # macOS Automated Bootstrapper Installer
├── launch.vbs             # Windows Hidden Console Window Wrapper
├── make_icon.py           # Cross-Platform Graphic Assets Compiler
├── assets/                # Auto-compiled Multi-Resolution Icon Folder
└── tabs/                  # Main Panel Module Controllers Package
    ├── geometry.py
    ├── effects.py
    ├── raw.py
    ├── batch.py
    ├── documentation.py
    ├── geometry_cogs/     # Independent Submodule Views
    ├── effects_cogs/
    ├── raw_cogs/
    ├── batch_cogs/
    └── doc_cogs/
```

---

## 🚀 Automated Environment Workspace Setup

Clone the repository and run the setup bootstrapper script corresponding to your local host operating system. The installer automatically provisions core binaries and pulls down Python module tracking dependencies.

### 🔷 Windows Framework Users

1. Open your cloned repository folder.
2. Right-click **`setup.bat`** and choose **"Run as administrator"** (Required to register environment variables).

### 🐧 Linux Environment Users

Open your command terminal line and execute:

```bash
chmod +x setup_linux.sh
sudo ./setup_linux.sh
```

### 🍏 macOS Architecture Users

Open your standard user command terminal window (**Do not run this script using sudo**) and execute:

```bash
chmod +x setup_mac.sh
./setup_mac.sh
```

---

## 🏁 Launching the Studio Application

Once your deployment bootstrapper finishes successfully, spin up the unified workspace app container:

```bash
python main.py
```

*(On Windows systems, you can simply double-click the **`launch.vbs`** script file to pop the GUI interface open instantly with zero background command prompt terminal windows appearing.)*

---

## 🧰 Prerequisites / Manual Adjustments

If you choose not to use the automated system bootstrappers, ensure these target core components are installed manually on your device and bound to your System PATH variables:

* **Python:** Runtime Engine (v3.10 or higher).
* **ImageMagick:** CLI Core Utility Toolkit Binary.
* **Python Modules:** `pip install customtkinter pillow`.

---

## 🤝 Contributing

Contributions, bug reports, parameter updates, and custom sub-cogs features tracking ideas are completely welcome! Feel free to fork the framework package layers, modify view elements on top-level layout trees, and open a remote Pull Request pass cleanly.
