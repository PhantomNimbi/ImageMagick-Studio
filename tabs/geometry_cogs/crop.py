import customtkinter as ctk

class CropCog(ctk.CTkFrame):
    def __init__(self, parent, engine, txt_in, txt_out):
        super().__init__(parent, fg_color="transparent")
        self.engine = engine
        self.txt_in = txt_in
        self.txt_out = txt_out

        # Advanced Crop Parameters Matrix
        self.chk_crop = ctk.CTkCheckBox(self, text="Crop Box Area (-crop)")
        self.chk_crop.select()
        self.chk_crop.grid(row=0, column=0, sticky="w", padx=20, pady=10)
        self.txt_crop = ctk.CTkEntry(self, width=150)
        self.txt_crop.insert(0, "400x400+0+0")
        self.txt_crop.grid(row=0, column=1, sticky="w", padx=10, pady=10)

        lbl_grav = ctk.CTkLabel(self, text="Gravity Coordinate Anchor (-gravity):")
        lbl_grav.grid(row=1, column=0, sticky="w", padx=20, pady=10)
        self.cmb_grav = ctk.CTkOptionMenu(self, values=["None", "Center", "North", "East", "South", "West", "NorthEast", "NorthWest", "SouthEast", "SouthWest"], width=150)
        self.cmb_grav.set("None")
        self.cmb_grav.grid(row=1, column=1, sticky="w", padx=10, pady=10)

        self.chk_repage = ctk.CTkCheckBox(self, text="Reset Canvas Offsets (+repage)")
        self.chk_repage.select()
        self.chk_repage.grid(row=2, column=0, columnspan=2, sticky="w", padx=20, pady=10)

        self.btn_fire = ctk.CTkButton(self, text="Execute Crop Selection", font=ctk.CTkFont(size=14, weight="bold"), command=self.run)
        self.btn_fire.grid(row=5, column=0, columnspan=2, pady=30, sticky="ew", padx=20)

    def run(self):
        if not self.txt_in.get().strip(): return
        args = f'"{self.txt_in.get()}"'
        if self.cmb_grav.get() != "None": args += f' -gravity {self.cmb_grav.get()}'
        if self.chk_crop.get(): args += f' -crop {self.txt_crop.get()}'
        if self.chk_repage.get(): args += ' +repage'
        args += f' "{self.txt_out.get()}"'
        self.engine.invoke_magick(args)
