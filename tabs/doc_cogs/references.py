import customtkinter as ctk

class ReferencesCog(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        txt = ctk.CTkTextbox(self, font=ctk.CTkFont(family="Segoe UI", size=11))
        txt.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        txt.insert("1.0", "Geometry Modifications (-resize)\n\n"
                          "[-] Sizing Box Constraints\n"
                          "Provide exact widths and heights parameters (e.g. 1920x1080). Image files resample "
                          "proportionally to fit the dimensions.\n\n"
                          "[-] Ratio Scales\n"
                          "Append percent operators (e.g. 50%) to shrink assets down by half.")
        txt.configure(state="disabled")
