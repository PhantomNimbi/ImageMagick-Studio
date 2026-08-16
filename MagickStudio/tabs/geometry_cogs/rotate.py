import customtkinter as ctk

class RotateCog(ctk.CTkFrame):
    def __init__(self, parent, engine, txt_in, txt_out):
        super().__init__(parent, fg_color="transparent")
        self.engine = engine
        self.txt_in = txt_in
        self.txt_out = txt_out

        # Orientation Modifications Matrix
        self.chk_rot = ctk.CTkCheckBox(self, text="Rotate Angle Degrees (-rotate)")
        self.chk_rot.grid(row=0, column=0, sticky="w", padx=20, pady=10)
        self.txt_rot = ctk.CTkEntry(self, width=150)
        self.txt_rot.insert(0, "90")
        self.txt_rot.grid(row=0, column=1, sticky="w", padx=10, pady=10)

        self.chk_flip = ctk.CTkCheckBox(self, text="Vertical Invert Flip (-flip)")
        self.chk_flip.grid(row=1, column=0, columnspan=2, sticky="w", padx=20, pady=10)

        self.chk_flop = ctk.CTkCheckBox(self, text="Horizontal Mirror Flop (-flop)")
        self.chk_flop.grid(row=2, column=0, columnspan=2, sticky="w", padx=20, pady=10)

        self.btn_fire = ctk.CTkButton(self, text="Execute Orientation Adjust", font=ctk.CTkFont(size=14, weight="bold"), command=self.run)
        self.btn_fire.grid(row=5, column=0, columnspan=2, pady=30, sticky="ew", padx=20)

    def run(self):
        if not self.txt_in.get().strip(): return
        args = f'"{self.txt_in.get()}"'
        if self.chk_rot.get(): args += f' -rotate {self.txt_rot.get()}'
        if self.chk_flip.get(): args += ' -flip'
        if self.chk_flop.get(): args += ' -flop'
        args += f' "{self.txt_out.get()}"'
        self.engine.invoke_magick(args)
