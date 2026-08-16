import customtkinter as ctk
from tkinter import filedialog

class PathsCog(ctk.CTkFrame):
    def __init__(self, parent, batch_state):
        super().__init__(parent, fg_color="transparent")
        self.batch_state = batch_state

        lbl_src = ctk.CTkLabel(self, text="Input Directory Folder Source:")
        lbl_src.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 5))
        
        self.txt_src = ctk.CTkEntry(self, width=420)
        self.txt_src.insert(0, self.batch_state["src_dir"])
        self.txt_src.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")
        
        btn_src = ctk.CTkButton(self, text="Select Source...", width=120, command=lambda: self.pick_dir(self.txt_src, "src_dir"))
        btn_src.grid(row=0, column=2, padx=(0, 20), pady=(20, 5))

        lbl_dst = ctk.CTkLabel(self, text="Output Directory Target:")
        lbl_dst.grid(row=1, column=0, sticky="w", padx=20, pady=5)
        
        self.txt_dst = ctk.CTkEntry(self, width=420)
        self.txt_dst.insert(0, self.batch_state["dst_dir"])
        self.txt_dst.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        btn_dst = ctk.CTkButton(self, text="Select Target...", width=120, command=lambda: self.pick_dir(self.txt_dst, "dst_dir"))
        btn_dst.grid(row=1, column=2, padx=(0, 20), pady=5)

    def pick_dir(self, entry_widget, state_key):
        d = filedialog.askdirectory()
        if d:
            entry_widget.delete(0, "end")
            entry_widget.insert(0, d)
            self.batch_state[state_key] = d
