import customtkinter as ctk

class GuideCog(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        
        # Grid weight configuration to ensure fluid resizing layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        txt = ctk.CTkTextbox(self, font=ctk.CTkFont(family="Segoe UI", size=11))
        txt.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        txt.insert("1.0", "Studio Application User Guide\n\n"
                          "[-] Interface Basics\n"
                          "Select images using the browse parameters button options. Configure modifiers, "
                          "and execute scripts to process.\n\n"
                          "[-] Mass Directory Automation\n"
                          "Point paths at an input folder library, apply target matching extensions filters "
                          "(like .png) and run mass loops.")
        txt.configure(state="disabled")
