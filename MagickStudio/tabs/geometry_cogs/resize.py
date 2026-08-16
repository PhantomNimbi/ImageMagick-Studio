import customtkinter as ctk

class ResizeCog(ctk.CTkFrame):
    def __init__(self, parent, engine, txt_in, txt_out):
        super().__init__(parent, fg_color="transparent")
        self.engine = engine
        self.txt_in = txt_in
        self.txt_out = txt_out

        # Local Operation Checkboxes & Inputs
        self.chk_resize = ctk.CTkCheckBox(self, text="Resize Sizing (-resize)")
        self.chk_resize.select()
        self.chk_resize.grid(row=0, column=0, sticky="w", padx=20, pady=10)
        
        self.txt_resize = ctk.CTkEntry(self, width=150)
        self.txt_resize.insert(0, "1920x1080")
        self.txt_resize.grid(row=0, column=1, sticky="w", padx=10, pady=10)

        self.chk_scale = ctk.CTkCheckBox(self, text="Scale Factor (-scale)")
        self.chk_scale.grid(row=1, column=0, sticky="w", padx=20, pady=10)
        
        self.txt_scale = ctk.CTkEntry(self, width=150)
        self.txt_scale.insert(0, "50%")
        self.txt_scale.grid(row=1, column=1, sticky="w", padx=10, pady=10)

        # Action Submission Trigger
        self.btn_fire = ctk.CTkButton(self, text="Execute Image Resizing", font=ctk.CTkFont(size=14, weight="bold"), command=self.run)
        self.btn_fire.grid(row=5, column=0, columnspan=2, pady=30, sticky="ew", padx=20)

    def run(self):
        if not self.txt_in.get().strip(): return
        args = f'"{self.txt_in.get()}"'
        if self.chk_resize.get(): args += f' -resize {self.txt_resize.get()}'
        if self.chk_scale.get(): args += f' -scale {self.txt_scale.get()}'
        args += f' "{self.txt_out.get()}"'
        self.engine.invoke_magick(args)
