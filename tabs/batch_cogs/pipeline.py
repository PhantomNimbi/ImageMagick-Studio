import os
import customtkinter as ctk

class PipelineCog(ctk.CTkFrame):
    def __init__(self, parent, engine, batch_state):
        super().__init__(parent, fg_color="transparent")
        self.engine = engine
        self.batch_state = batch_state

        lbl_flt = ctk.CTkLabel(self, text="Search Extension Match Wildcard:")
        lbl_flt.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 5))
        
        self.txt_flt = ctk.CTkEntry(self, width=150)
        self.txt_flt.insert(0, self.batch_state["filter"])
        self.txt_flt.grid(row=0, column=1, sticky="w", padx=10, pady=(20, 5))

        lbl_args = ctk.CTkLabel(self, text="Global Operations Filters Chain:")
        lbl_args.grid(row=1, column=0, sticky="w", padx=20, pady=5)
        
        self.txt_args = ctk.CTkEntry(self, width=580, font=ctk.CTkFont(family="Consolas"))
        self.txt_args.insert(0, self.batch_state["args"])
        self.txt_args.grid(row=2, column=0, columnspan=3, sticky="w", padx=20, pady=5)

        lbl_ext = ctk.CTkLabel(self, text="Output Casting Format Extension:")
        lbl_ext.grid(row=3, column=0, sticky="w", padx=20, pady=5)
        
        self.txt_ext = ctk.CTkEntry(self, width=150)
        self.txt_ext.insert(0, self.batch_state["ext"])
        self.txt_ext.grid(row=3, column=1, sticky="w", padx=10, pady=5)

        btn_run = ctk.CTkButton(self, text="Initialize Folder Batch Loop", font=ctk.CTkFont(size=14, weight="bold"), command=self.fire_batch)
        btn_run.grid(row=4, column=0, columnspan=2, padx=20, pady=30, sticky="ew")

    def sync_state(self):
        """Saves current input text configurations down to global tracking maps."""
        self.batch_state["filter"] = self.txt_flt.get()
        self.batch_state["args"] = self.txt_args.get()
        self.batch_state["ext"] = self.txt_ext.get()

    def fire_batch(self):
        self.sync_state()
        src, dst = self.batch_state["src_dir"], self.batch_state["dst_dir"]
        
        if not src or not dst or not os.path.exists(src) or not os.path.exists(dst):
            self.engine.log("[ERROR]: Sourcing paths verification failed. Ensure valid folders are picked under Tab 1.")
            return
        
        filter_str = self.batch_state["filter"].strip()
        if filter_str.startswith("*"): 
            filter_str = filter_str[1:]
        
        files = [f for f in os.listdir(src) if f.lower().endswith(filter_str.lower())]
        if not files:
            self.engine.log(f"[BATCH]: Zero matching items detected for extension filter: {filter_str}")
            return
            
        for f in files:
            full_in = os.path.join(src, f)
            name_base = os.path.splitext(f)[0]
            full_out = os.path.join(dst, name_base + self.batch_state["ext"].strip())
            self.engine.invoke_magick(f'"{full_in}" {self.batch_state["args"]} "{full_out}"')
