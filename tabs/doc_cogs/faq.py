import customtkinter as ctk

class FaqCog(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        txt = ctk.CTkTextbox(self, font=ctk.CTkFont(family="Segoe UI", size=11))
        txt.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        txt.insert("1.0", "Frequently Asked Questions\n\n"
                          "Q: Why am I getting an error saying 'magick CLI not found'?\n"
                          "A: Verify ImageMagick installer was run and option box 'Add directory to system PATH' "
                          "was explicitly checked.\n\n"
                          "Q: Why do transparent shapes turn back into black fills?\n"
                          "A: Containers like JPEGs do not carry alpha channel data. Pre-append flat background "
                          "colors (e.g. -background white -alpha remove) before executing formatting casts.")
        txt.configure(state="disabled")
