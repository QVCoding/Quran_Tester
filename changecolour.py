from PIL import Image, ImageOps
from pathlib import Path

# ============================================================
# SETTINGS
# ============================================================

NEW_COLOUR = "#ede6d6"

# ============================================================

script_dir = Path(__file__).resolve().parent

png_files = list(script_dir.glob("*.png"))

if not png_files:
    print("No PNG files found.")
    input("Press Enter to exit...")
    raise SystemExit

for png_path in png_files:
    image = Image.open(png_path).convert("RGBA")

    # Extract alpha channel
    alpha = image.getchannel("A")

    # Create a solid image of the new colour
    new_image = Image.new("RGBA", image.size, NEW_COLOUR)

    # Put the original alpha back
    new_image.putalpha(alpha)

    # Overwrite the original
    new_image.save(png_path, optimize=True)

    print(f"Changed: {png_path.name}")

print("\nDone.")
input("Press Enter to exit...")