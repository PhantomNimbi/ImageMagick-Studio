import subprocess
import shutil
import customtkinter as ctk

# Ensure CustomTkinter matches the user's OS preference
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class CoreEngine:
    def __init__(self, console_widget):
        self.console = console_widget

    def log(self, message):
        """Streams system diagnostics directly to the main terminal log."""
        self.console.configure(state="normal")
        self.console.insert("end", f"{message}\n")
        self.console.ensure_line_visible(self.console.index("end-1c"))
        self.console.configure(state="disabled")

    def invoke_magick(self, argument_string):
        """Runs the ImageMagick CLI process safely with detailed error mapping."""
        self.log(f"\n[EXEC]: magick {argument_string}")
        
        # Verify ImageMagick binary is discoverable in system PATH
        if not shutil.which("magick"):
            self.log("[ERROR]: 'magick' CLI binary not found. Please install ImageMagick and add it to your System PATH variables.")
            return

        try:
            # Parse arguments cleanly while safeguarding shell variables
            cmd = ["magick"] + subprocess.split(argument_string)
            process = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=False
            )
            stdout, stderr = process.communicate()

            if stdout.strip():
                self.log(f"[OUTPUT]: {stdout.strip()}")
            if stderr.strip():
                self.log(f"[ERROR]: {stderr.strip()}")
            
            if process.returncode == 0:
                self.log("[SUCCESS]: Operation completed error-free.")
            else:
                self.log(f"[FAILURE]: Exited with systemic return code {process.returncode}")
        except Exception as e:
            self.log(f"[SYSTEM CRASH]: Critical loop exception caught: {str(e)}")
