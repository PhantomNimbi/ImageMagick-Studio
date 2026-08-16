import os
import customtkinter as ctk
from tkinter import filedialog
from tabs.effects_cogs.quality import QualityCog
from tabs.effects_cogs.blur import BlurCog
from tabs.effects_cogs.colorspace import ColorspaceCog
from tabs.effects_cogs.filters import FiltersCog

class EffectsModule(ctk.CTkFrame):
    def __init__(self, parent, engine):
        super().__init__(parent, fg_color="transparent")
        self.engine = engine
        self.idx_frame = ctk.CTkFrame(self, width=240, corner_radius=8)
        self.idx_frame.pack(side="left", fill="y", padx=(10, 10), pady=10)
        self.idx_frame.pack_propagate(False)

        lbl_index = ctk.CTkLabel(self.idx_frame, text="Visual Effects Index:", font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"))
        lbl_index.pack(anchor="w", padx=15, pady=(15, 10))

        # Fully mapped out category keys list
        cogs = ["1. Quality & Compression", "2. Blur & Sharpen Filters", "3. Force Colorspace Channels", "4. Artistic Matrix Filters"]
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
                txt_out.delete(0, "end"); txt_out.insert(0, os.path.splitext(file) + "_fx.png")

        btn_browse = ctk.CTkButton(self.view_box, text="Browse...", width=100, command=browse)
        btn_browse.grid(row=0, column=2, padx=(0, 20), pady=(20, 5))
        lbl_out = ctk.CTkLabel(self.view_box, text="Output Destination:")
        lbl_out.grid(row=1, column=0, sticky="w", padx=20, pady=5)
        txt_out = ctk.CTkEntry(self.view_box, width=420)
        txt_out.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        cog_container = ctk.CTkFrame(self.view_box, fg_color="transparent")
        cog_container.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=0, pady=10)
        cog_container.grid_columnconfigure(0, weight=1)
        cog_container.grid_rowconfigure(0, weight=1)

        if index == 0: QualityCog(cog_container, self.engine, txt_in, txt_out).grid(row=0, column=0, sticky="nsew")
        elif index == 1: BlurCog(cog_container, self.engine, txt_in, txt_out).grid(row=0, column=0, sticky="nsew")
        elif index == 2: ColorspaceCog(cog_container, self.engine, txt_in, txt_out).grid(row=0, column=0, sticky="nsew")
        elif index == 3: FiltersCog(cog_container, self.engine, txt_in, txt_out).grid(row=0, column=0, sticky="nsew")
