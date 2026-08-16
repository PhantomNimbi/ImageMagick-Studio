import customtkinter as ctk

class ExtentCog(ctk.CTkFrame):
    def __init__(self, parent, engine, txt_in, txt_out):
        super().__init__(parent, fg_color="transparent")
        self.engine = engine
        self.txt_in = txt_in
        self.txt_out = txt_out

        # Canvas Resizing & Margin Parameters
        self.chk_ext = ctk.CTkCheckBox(self, text="Canvas Frame Target (-extent)")
        self.chk_ext.select()
        self.chk_ext.grid(row=0, column=0, sticky="w", padx=20, pady=10)
        self.txt_ext = ctk.CTkEntry(self, width=150)
        self.txt_ext.insert(0, "1000x1000")
        self.txt_ext.grid(row=0, column=1, sticky="w", padx=10, pady=10)

        self.chk_bg = ctk.CTkCheckBox(self, text="Background Canvas Fill (-background)")
        self.chk_bg.select()
        self.chk_bg.grid(row=1, column=0, sticky="w", padx=20, pady=10)
        self.txt_bg = ctk.CTkEntry(self, width=150)
        self.txt_bg.insert(0, "white")
        self.txt_bg.grid(row=1, column=1, sticky="w", padx=10, pady=10)

        lbl_grav = ctk.CTkLabel(self, text="Gravity Alignment Origin:")
        lbl_grav.grid(row=2, column=0, sticky="w", padx=20, pady=10)
        self.cmb_grav = ctk.CTkOptionMenu(self, values=["None", "Center", "North", "East", "South", "West"], width=150)
        self.cmb_grav.set("Center")
        self.cmb_grav.grid(row=2, column=1, sticky="w", padx=10, pady=10)

        self.btn_fire = ctk.CTkButton(self, text="Execute Canvas Extent", font=ctk.CTkFont(size=14, weight="bold"), command=self.run)
        self.btn_fire.grid(row=5, column=0, columnspan=2, pady=30, sticky="ew", padx=20)

    def run(self):
        if not self.txt_in.get().strip(): return
        args = f'"{self.txt_in.get()}"'
        if self.chk_bg.get(): args += f' -background {self.txt_bg.get()}'
        if self.cmb_grav.get() != "None": args += f' -gravity {self.cmb_grav.get()}'
        if self.chk_ext.get(): args += f' -extent {self.txt_ext.get()}'
        args += f' "{self.txt_out.get()}"'
        self.engine.invoke_magick(args)
