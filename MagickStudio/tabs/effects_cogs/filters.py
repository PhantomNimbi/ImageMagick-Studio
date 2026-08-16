import customtkinter as ctk

class FiltersCog(ctk.CTkFrame):
    def __init__(self, parent, engine, txt_in, txt_out):
        super().__init__(parent, fg_color="transparent")
        self.engine = engine
        self.txt_in = txt_in
        self.txt_out = txt_out

        # Advanced Stylization Layer Routing Matrix
        lbl_art = ctk.CTkLabel(self, text="Artistic Convolution Matrix Filters:")
        lbl_art.grid(row=0, column=0, sticky="w", padx=20, pady=10)
        self.cmb_art = ctk.CTkOptionMenu(self, values=["None", "-monochrome", "-negate", "-charcoal 2", "-edge 2", "-emboss 2", "-solarize 50%", "-enhance"], width=180)
        self.cmb_art.set("-charcoal 2")
        self.cmb_art.grid(row=0, column=1, sticky="w", padx=10, pady=10)

        self.chk_modulate = ctk.CTkCheckBox(self, text="Tone Modulation (-modulate Bright,Sat,Hue)")
        self.chk_modulate.grid(row=1, column=0, sticky="w", padx=20, pady=10)
        self.txt_modulate = ctk.CTkEntry(self, width=180)
        self.txt_modulate.insert(0, "100,100,100")
        self.txt_modulate.grid(row=1, column=1, sticky="w", padx=10, pady=10)

        self.btn_fire = ctk.CTkButton(self, text="Render Artistic Pass", font=ctk.CTkFont(size=14, weight="bold"), command=self.run)
        self.btn_fire.grid(row=5, column=0, columnspan=2, pady=30, sticky="ew", padx=20)

    def run(self):
        if not self.txt_in.get().strip(): return
        args = f'"{self.txt_in.get()}"'
        if self.cmb_art.get() != "None": args += f' {self.cmb_art.get()}'
        if self.chk_modulate.get(): args += f' -modulate {self.txt_modulate.get()}'
        args += f' "{self.txt_out.get()}"'
        self.engine.invoke_magick(args)
