import customtkinter as ctk
from tkinter import filedialog

class IdentifyCog(ctk.CTkFrame):
    def __init__(self, parent, engine):
        super().__init__(parent, fg_color="transparent")
        self.engine = engine

        lbl_desc = ctk.CTkLabel(self, text="Extract comprehensive metadata arrays, channel maps, density rows, and EXIF tables.", justify="left")
        lbl_desc.pack(anchor="w", padx=20, pady=(20, 10))

        btn_id = ctk.CTkButton(self, text="Browse Image & Run Introspection", font=ctk.CTkFont(size=13, weight="bold"), command=self.run)
        btn_id.pack(anchor="w", padx=20, pady=10)

    def run(self):
        f = filedialog.askopenfilename()
        if f:
            self.engine.invoke_magick(f'identify -verbose "{f}"')
