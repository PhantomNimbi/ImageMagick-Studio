import os
import customtkinter as ctk
from tkinter import filedialog

# Explicitly pull cogs using the flat root tabs directory namespace
from tabs.geometry_cogs.resize import ResizeCog
from tabs.geometry_cogs.crop import CropCog
from tabs.geometry_cogs.extent import ExtentCog
from tabs.geometry_cogs.rotate import RotateCog

class GeometryModule(ctk.CTkFrame):
    def __init__(self, parent, engine):
        super().__init__(parent, fg_color="transparent")
        self.engine = engine
        self.idx_frame = ctk.CTkFrame(self, width=240, corner_radius=8)
        self.idx_frame.pack(side="left", fill="y", padx=(10, 10), pady=10)
        self.idx_frame.pack_propagate(False)

        lbl_index = ctk.CTkLabel(self.idx_frame, text="Geometry Categories:", font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"))
        lbl_index.pack(anchor="w", padx=15, pady=(15, 10))

        cogs = ["1. Resize & Pixel Scale", "2. Cropping Coordinates", "3. Canvas Borders & Extents", "4. Rotations & Flips"]
        for i, name in enumerate(cogs):
            btn = ctk.CTkButton(self.idx_frame, text=name, anchor="w", fg_color="transparent", text_color=("black", "white"), hover_color=("gray80", "gray25"), command=lambda idx=i: self.switch_view_box(idx))
            btn.pack(fill="x", padx=10, pady=2)

        self.view_box = ctk.CTkFrame(self, corner_radius=8)
        self.view_box.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=10)
        self.view_box.grid_columnconfigure(0, weight=1)
        self.view_box.grid_rowconfigure(0, weight=1)

        self.switch_view_box(0)

    def switch_view_box(self, index):
        for widget in self.view_box.winfo_children(): widget.destroy()
        lbl_in = ctk.CTkLabel(self.view_box, text="Source File:")
        lbl_in.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 5))
        txt_in = ctk.CTkEntry(self.view_box, width=420)
        txt_in.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")
        
        def browse():
            file = filedialog.askopenfilename()
            if file:
                txt_in.delete(0, "end"); txt_in.insert(0, file)
                txt_out.delete(0, "end"); txt_out.insert(0, os.path.splitext(file) + "_mod.jpg")

        btn_browse = ctk.CTkButton(self.view_box, text="Browse...", width=100, command=browse)
        btn_browse.grid(row=0, column=2, padx=(0, 20), pady=(20, 5))
        lbl_out = ctk.CTkLabel(self.view_box, text="Output Target:")
        lbl_out.grid(row=1, column=0, sticky="w", padx=20, pady=5)
        txt_out = ctk.CTkEntry(self.view_box, width=420)
        txt_out.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        cog_container = ctk.CTkFrame(self.view_box, fg_color="transparent")
        cog_container.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=0, pady=10)
        cog_container.grid_columnconfigure(0, weight=1)
        cog_container.grid_rowconfigure(0, weight=1)

        if index == 0: ResizeCog(cog_container, self.engine, txt_in, txt_out).grid(row=0, column=0, sticky="nsew")
        elif index == 1: CropCog(cog_container, self.engine, txt_in, txt_out).grid(row=0, column=0, sticky="nsew")
        elif index == 2: ExtentCog(cog_container, self.engine, txt_in, txt_out).grid(row=0, column=0, sticky="nsew")
        elif index == 3: RotateCog(cog_container, self.engine, txt_in, txt_out).grid(row=0, column=0, sticky="nsew")
