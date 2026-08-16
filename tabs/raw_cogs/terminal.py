import customtkinter as ctk

class TerminalCog(ctk.CTkFrame):
    def __init__(self, parent, engine):
        super().__init__(parent, fg_color="transparent")
        self.engine = engine

        lbl_raw = ctk.CTkLabel(self, text="Unrestricted Parameter String (Appended directly after 'magick '):")
        lbl_raw.pack(anchor="w", padx=20, pady=(20, 5))
        
        self.txt_raw = ctk.CTkEntry(self, width=640, font=ctk.CTkFont(family="Consolas", size=11))
        self.txt_raw.insert(0, "source.png -resize 50% -rotate 90 output.jpg")
        self.txt_raw.pack(anchor="w", padx=20, pady=5)

        btn_run = ctk.CTkButton(self, text="Fire Shell Pipeline execution", font=ctk.CTkFont(size=13, weight="bold"), command=self.run)
        btn_run.pack(anchor="w", padx=20, pady=20)

    def run(self):
        if self.txt_raw.get().strip():
            self.engine.invoke_magick(self.txt_raw.get())
