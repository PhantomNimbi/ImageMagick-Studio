import customtkinter as ctk

class QualityCog(ctk.CTkFrame):
    def __init__(self, parent, engine, txt_in, txt_out):
        super().__init__(parent, fg_color="transparent")
        self.engine = engine
        self.txt_in = txt_in
        self.txt_out = txt_out

        self.chk_qual = ctk.CTkCheckBox(self, text="Compression Quality (-quality)")
        self.chk_qual.select()
        self.chk_qual.grid(row=0, column=0, sticky="w", padx=20, pady=10)
        
        self.txt_qual = ctk.CTkEntry(self, width=150)
        self.txt_qual.insert(0, "85")
        self.txt_qual.grid(row=0, column=1, sticky="w", padx=10, pady=10)

        self.chk_strip = ctk.CTkCheckBox(self, text="Strip Profile Metadata (-strip)")
        self.chk_strip.grid(row=1, column=0, columnspan=2, sticky="w", padx=20, pady=10)

        # --- THE FIXED LINE ---
        # Changed 'xxx="ew"' to 'sticky="ew"' to prevent the Tkinter option parser crash.
        self.btn_fire = ctk.CTkButton(self, text="Execute Compression Matrix", font=ctk.CTkFont(size=14, weight="bold"), command=self.run)
        self.btn_fire.grid(row=5, column=0, columnspan=2, pady=30, sticky="ew", padx=20)

    def run(self):
        if not self.txt_in.get().strip(): return
        args = f'"{self.txt_in.get()}"'
        if self.chk_qual.get(): args += f' -quality {self.txt_qual.get()}'
        if self.chk_strip.get(): args += ' -strip'
        args += f' "{self.txt_out.get()}"'
        self.engine.invoke_magick(args)
