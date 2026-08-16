import customtkinter as ctk

class ColorspaceCog(ctk.CTkFrame):
    def __init__(self, parent, engine, txt_in, txt_out):
        super().__init__(parent, fg_color="transparent")
        self.engine = engine
        self.txt_in = txt_in
        self.txt_out = txt_out

        lbl_space = ctk.CTkLabel(self, text="Target Chromatic Profile:")
        lbl_space.grid(row=0, column=0, sticky="w", padx=20, pady=10)
        self.cmb_space = ctk.CTkOptionMenu(self, values=["sRGB", "Gray", "CMYK", "RGB", "HSL"], width=150)
        self.cmb_space.set("Gray")
        self.cmb_space.grid(row=0, column=1, sticky="w", padx=10, pady=10)

        self.btn_fire = ctk.CTkButton(self, text="Map Colorspace Channels", font=ctk.CTkFont(size=14, weight="bold"), command=self.run)
        self.btn_fire.grid(row=5, column=0, columnspan=2, pady=30, sticky="ew", padx=20)

    def run(self):
        if not self.txt_in.get().strip(): return
        args = f'"{self.txt_in.get()}" -colorspace {self.cmb_space.get()} "{self.txt_out.get()}"'
        self.engine.invoke_magick(args)
