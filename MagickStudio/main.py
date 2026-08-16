import os
import sys
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
        # Selects the optimal asset format based on the host operating system platform
        assets_dir = "assets"
        
        if sys.platform.startswith("win"):
            # Windows: Load standard multi-resolution ICO file container
            icon_win = os.path.join(assets_dir, "app_icon.ico")
            if os.path.exists(icon_win):
                self.wm_iconbitmap(icon_win)
                
        elif sys.platform.startswith("darwin"):
            # macOS: Load standardized Apple ICNS container layer
            icon_mac = os.path.join(assets_dir, "app_icon.icns")
            if os.path.exists(icon_mac):
                # CustomTkinter wraps standard Tkinter icon photo methods for Apple hosts
                try:
                    self.iconbitmap(icon_mac)
                except Exception:
                    pass
                    
        else:
            # Linux / X11 / Wayland: Load standalone high-res 256x256 PNG raster layer
            icon_linux = os.path.join(assets_dir, "icon_256x256.png")
            if os.path.exists(icon_linux):
                try:
                    img_object = ctk.CTkImage(light_image=None, dark_image=None) # Placeholder initialization
                    # Pass raw photo image data map up to the X11 windowing subsystem
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
