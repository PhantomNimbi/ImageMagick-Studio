import os
from PIL import Image, ImageDraw

def generate_studio_assets():
    # 1. Enforce and prepare a clean assets subfolder path
    assets_dir = "assets"
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)
        print(f"[*] Created target assets directory at: {os.path.abspath(assets_dir)}")

    # 2. Initialize the master 256x256 high-resolution icon canvas
    icon_size = (256, 256)
    img = Image.new("RGBA", icon_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 3. Draw a modern, soft-edged rounded rectangle tile background
    bg_color = (22, 27, 34, 255)
    draw.rounded_rectangle([16, 16, 240, 240], radius=45, fill=bg_color)

    # 4. Draw an enterprise accent boundary frame track
    accent_color = (31, 111, 235, 255)
    draw.rounded_rectangle([16, 16, 240, 240], radius=45, outline=accent_color, width=6)

    # 5. Draw a stylized magic editing wand element shape
    # The Handle (Deep Gray)
    draw.polygon([(60, 200), (75, 185), (135, 245), (120, 260)], fill=(70, 75, 80, 255))
    # The Shaft (Polished Silver)
    draw.line([90, 170, 170, 90], fill=(210, 215, 220, 255), width=14)
    # The Tip / Lens Aperture Cap (Neon Cyan / Mint Green Highlight)
    draw.ellipse([160, 70, 195, 105], fill=(57, 211, 83, 255))

    # 6. Draw digital vector pixels / geometric transformation markers
    draw.rectangle([50, 60, 75, 85], fill=(31, 111, 235, 180))      # Outer Blue Cluster
    draw.rectangle([85, 40, 105, 60], fill=(57, 211, 83, 140))      # Mint Green Cluster
    draw.rectangle([200, 140, 220, 160], fill=(31, 111, 235, 200))  # Right Side Cluster

    print("[*] Master canvas drawn completely. Beginning cross-platform asset packaging...")

    # ==========================================================================
    # PIPELINE 1: WINDOWS OS EXPORT (.ICO Multi-Resolution Container)
    # ==========================================================================
    ico_sizes = [16, 32, 48, 64, 128, 256]
    ico_path = os.path.join(assets_dir, "app_icon.ico")
    img.save(ico_path, format="ICO", sizes=[(s, s) for s in ico_sizes])
    print(f"[✓] Windows asset bundled successfully at: {ico_path}")

    # ==========================================================================
    # PIPELINE 2: MACOS APPLE EXPORT (.ICNS Standardized Block Verification)
    # ==========================================================================
    # Apple .icns packaging strictly requires a specific set of standardized resolution blocks.
    # We pass these exact sizes to prevent Pillow from throwing a block generation error.
    icns_sizes = [16, 32, 64, 128, 256]
    icns_path = os.path.join(assets_dir, "app_icon.icns")
    img.save(icns_path, format="ICNS", sizes=[(s, s) for s in icns_sizes])
    print(f"[✓] macOS asset bundled successfully at: {icns_path}")

    # ==========================================================================
    # PIPELINE 3: LINUX OPEN-SOURCE EXPORT (Discrete Standalone PNG Rasters)
    # ==========================================================================
    # Linux distributions check for standalone size-labeled PNG files inside app folders.
    linux_sizes = [16, 32, 48, 64, 128, 256]
    for size in linux_sizes:
        resized_img = img.resize((size, size), resample=Image.Resampling.LANCZOS)
        linux_png_path = os.path.join(assets_dir, f"icon_{size}x{size}.png")
        resized_img.save(linux_png_path, format="PNG")
        
    print(f"[✓] Linux raster assets mapped completely into: {os.path.abspath(assets_dir)}")
    print("\n" + "=" * 60)
    print("[SUCCESS]: Asset generation complete for cross-platform deployment!")
    print("=" * 60)

if __name__ == "__main__":
    generate_studio_assets()
