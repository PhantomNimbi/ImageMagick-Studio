import customtkinter as ctk

class BlurCog(ctk.CTkFrame):
    def __init__(self, parent, engine, txt_in, txt_out):
        super().__init__(parent, fg_color="transparent")
        self.engine = engine
        self.txt_in = txt_in
        self.txt_out = txt_out

        # Convolution Sharpness & Softness Parameters
        self.chk_blur = ctk.CTkCheckBox(self, text="Gaussian Blur Density (-blur)")
        self.chk_blur.grid(row=0, column=0, sticky="w", padx=20, pady=10)
        self.txt_blur = ctk.CTkEntry(self, width=150)
        self.txt_blur.insert(0, "0x5")
        self.txt_blur.grid(row=0, column=1, sticky="w", padx=10, pady=10)

        self.chk_sharp = ctk.CTkCheckBox(self, text="Adaptive Sharpening (-sharpen)")
        self.chk_sharp.grid(row=1, column=0, sticky="w", padx=20, pady=10)
        self.txt_sharp = ctk.CTkEntry(self, width=150)
        self.txt_sharp.insert(0, "0x1")
        self.txt_sharp.grid(row=1, column=1, sticky="w", padx=10, pady=10)

        self.chk_radial = ctk.CTkCheckBox(self, text="Radial Blur Factor (-radial-blur)")
        self.chk_radial.grid(row=2, column=0, sticky="w", padx=20, pady=10)
        self.txt_radial = ctk.CTkEntry(self, width=150)
        self.txt_radial.insert(0, "10")
        self.txt_radial.grid(row=2, column=1, sticky="w", padx=10, pady=10)

        self.btn_fire = ctk.CTkButton(self, text="Execute Convolution Kernel", font=ctk.CTkFont(size=14, weight="bold"), command=self.run)
        self.btn_fire.grid(row=5, column=0, columnspan=2, pady=30, sticky="ew", padx=20)

    def run(self):
        if not self.txt_in.get().strip(): return
        args = f'"{self.txt_in.get()}"'
        if self.chk_blur.get(): args += f' -blur {self.txt_blur.get()}'
        if self.chk_sharp.get(): args += f' -sharpen {self.txt_sharp.get()}'
        if self.chk_radial.get(): args += f' -radial-blur {self.txt_radial.get()}'
        args += f' "{self.txt_out.get()}"'
        self.engine.invoke_magick(args)
