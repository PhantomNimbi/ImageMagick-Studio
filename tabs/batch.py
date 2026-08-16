import customtkinter as ctk
from tabs.batch_cogs.paths import PathsCog
from tabs.batch_cogs.pipeline import PipelineCog

class BatchModule(ctk.CTkFrame):
    def __init__(self, parent, engine):
        super().__init__(parent, fg_color="transparent")
        self.engine = engine

        # Left Column List Index Selector
        self.idx_frame = ctk.CTkFrame(self, width=240, corner_radius=8)
        self.idx_frame.pack(side="left", fill="y", padx=(10, 10), pady=10)
        self.idx_frame.pack_propagate(False)

        lbl_index = ctk.CTkLabel(self.idx_frame, text="Automation Index:", font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"))
        lbl_index.pack(anchor="w", padx=15, pady=(15, 10))

        cogs = ["1. Directory Location Select", "2. Filters & Bulk Execution"]
        for i, name in enumerate(cogs):
            btn = ctk.CTkButton(self.idx_frame, text=name, anchor="w", fg_color="transparent", text_color=("black", "white"), hover_color=("gray80", "gray25"), command=lambda idx=i: self.switch_view_box(idx))
            btn.pack(fill="x", padx=10, pady=2)

        # Unified shared dictionary dictionary object to hold parameter texts safely across views
        self.batch_state = {
            "src_dir": "",
            "dst_dir": "",
            "filter": ".png",
            "args": "-resize 1280x720 -colorspace sRGB",
            "ext": ".jpg"
        }

        self.view_box = ctk.CTkFrame(self, corner_radius=8)
        self.view_box.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=10)
        self.view_box.grid_columnconfigure(0, weight=1)
        self.view_box.grid_rowconfigure(0, weight=1)

        self.switch_view_box(0)

    def switch_view_box(self, index):
        for widget in self.view_box.winfo_children(): 
            widget.destroy()
            
        if index == 0:
            PathsCog(self.view_box, self.batch_state).grid(row=0, column=0, sticky="nsew")
        elif index == 1:
            PipelineCog(self.view_box, self.engine, self.batch_state).grid(row=0, column=0, sticky="nsew")
