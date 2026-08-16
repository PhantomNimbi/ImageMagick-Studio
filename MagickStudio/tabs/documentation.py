import customtkinter as ctk

# Explicitly pull cogs from the accurate lower-case folder names mapping paths
from tabs.doc_cogs.guide import GuideCog
from tabs.doc_cogs.references import ReferencesCog
from tabs.doc_cogs.faq import FaqCog

class DocumentationModule(ctk.CTkFrame):
    def __init__(self, parent, engine):
        super().__init__(parent, fg_color="transparent")
        self.engine = engine

        # Left Column List Index Selector
        self.idx_frame = ctk.CTkFrame(self, width=240, corner_radius=8)
        self.idx_frame.pack(side="left", fill="y", padx=(10, 10), pady=10)
        self.idx_frame.pack_propagate(False)

        lbl_index = ctk.CTkLabel(self.idx_frame, text="Manual Guides:", font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"))
        lbl_index.pack(anchor="w", padx=15, pady=(15, 10))

        cogs = ["1. Studio Application User Guide", "2. Geometry Modifications", "3. FAQ & Troubleshooting"]
        for i, name in enumerate(cogs):
            btn = ctk.CTkButton(self.idx_frame, text=name, anchor="w", fg_color="transparent", text_color=("black", "white"), hover_color=("gray80", "gray25"), command=lambda idx=i: self.switch_view_box(idx))
            btn.pack(fill="x", padx=10, pady=2)

        # Right Side Content Box
        self.view_box = ctk.CTkFrame(self, corner_radius=8)
        self.view_box.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=10)
        self.view_box.grid_columnconfigure(0, weight=1)
        self.view_box.grid_rowconfigure(0, weight=1)

        self.switch_view_box(0)

    def switch_view_box(self, index):
        for widget in self.view_box.winfo_children():
            widget.destroy()

        # Instantiate cogs dynamically on strict thread grids
        if index == 0:
            GuideCog(self.view_box).grid(row=0, column=0, sticky="nsew")
        elif index == 1:
            ReferencesCog(self.view_box).grid(row=0, column=0, sticky="nsew")
        elif index == 2:
            FaqCog(self.view_box).grid(row=0, column=0, sticky="nsew")
