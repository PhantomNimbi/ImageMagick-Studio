import os
import sys

# --- FORCE PORTABLE LIBRARY BINDINGS ON EXECUTION BOOT ---
# Prepend the internal vendor library path into memory before UI modules load
script_dir = os.path.dirname(os.path.abspath(__file__))
vendor_path = os.path.join(script_dir, "vendor")
if os.path.exists(vendor_path):
    sys.path.insert(0, vendor_path)

import ctypes
import customtkinter as ctk
from core import CoreEngine

# --- Sourcing Package UI Cogs from Root Tabs Directory ---
from tabs.geometry import GeometryModule
from tabs.effects import EffectsModule
from tabs.raw import RawModule
from tabs.batch import BatchModule
from tabs.documentation import DocumentationModule

# --- FORCE WINDOWS TASKBAR SEPARATION ---
if sys.platform.startswith("win"):
    try:
        myappid = 'joshua.imagemagickstudio.gui.v1'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except Exception:
        pass

class ApplicationStudio(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ImageMagick Studio")
        self.geometry("1060x800")
        self.minsize(1000, 750)

        # --- DYNAMIC CROSS-PLATFORM NATIVE ICON ROUTER ---
        assets_dir = "assets"
        
        if sys.platform.startswith("win"):
            icon_win = os.path.join(assets_dir, "app_icon.ico")
            if os.path.exists(icon_win):
                self.wm_iconbitmap(icon_win)
                
        elif sys.platform.startswith("darwin"):
            icon_mac = os.path.join(assets_dir, "app_icon.icns")
            if os.path.exists(icon_mac):
                try:
                    self.iconbitmap(icon_mac)
                except Exception:
                    pass
        else:
            icon_linux = os.path.join(assets_dir, "icon_256x256.png")
            if os.path.exists(icon_linux):
                try:
                    from PIL import Image, ImageTk
                    photo = ImageTk.PhotoImage(Image.open(icon_linux))
                    self.wm_iconphoto(True, photo)
                except Exception:
                    pass

        # Top Log Diagnostic Container Panel
        pnl_top = ctk.CTkFrame(self, height=160, corner_radius=0)
        pnl_top.pack(side="top", fill="x")
        pnl_top.pack_propagate(False)

        lbl_log = ctk.CTkLabel(pnl_top, text="Execution Diagnostics Log", font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"))
        lbl_log.pack(anchor="w", padx=20, pady=(10, 2))

        console_widget = ctk.CTkTextbox(pnl_top, fg_color="black", text_color="#00ff8c", font=ctk.CTkFont(family="Consolas", size=11))
        console_widget.pack(fill="both", expand=True, padx=20, pady=(0, 15))
        console_widget.insert("1.0", f"[SYSTEM]: Cross-Platform Graphic Assets Initialized Successfully for platform context: {sys.platform}\n")
        console_widget.configure(state="disabled")

        # Initialize background processing communications thread via root core
        engine = CoreEngine(console_widget)

        # Tabs Layout Control Center
        tab_view = ctk.CTkTabview(self)
        tab_view.pack(fill="both", expand=True, padx=10, pady=(5, 10))

        t1 = tab_view.add("Geometry & Format")
        t2 = tab_view.add("Color & Effects")
        t3 = tab_view.add("Diagnostics & Raw CLI")
        t4 = tab_view.add("Mass Batch Processing")
        t5 = tab_view.add("Documentation")

        # Map interior cog instances into tab surfaces natively
        GeometryModule(t1, engine).pack(fill="both", expand=True)
        EffectsModule(t2, engine).pack(fill="both", expand=True)
        RawModule(t3, engine).pack(fill="both", expand=True)
        BatchModule(t4, engine).pack(fill="both", expand=True)
        DocumentationModule(t5, engine).pack(fill="both", expand=True)

if __name__ == "__main__":
    app = ApplicationStudio()
    app.mainloop()
