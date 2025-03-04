import os
from pillow_heif import open_heif
from PIL import Image

def convert_heic_to_png(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return
    
    heic_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.heic')]

    if not heic_files:
        print("No HEIC files found in the folder.")
        return

    for heic_file in heic_files:
        heic_path = os.path.join(folder_path, heic_file)
        png_filename = os.path.splitext(heic_file)[0] + ".png"
        png_path = os.path.join(folder_path, png_filename)

        try:
            heif_image = open_heif(heic_path)
            image = Image.frombytes(
                heif_image.mode, heif_image.size, heif_image.data, "raw", heif_image.mode
            )
            image.save(png_path, "PNG")
            print(f"Converted: {heic_file} -> {png_filename}")
        except Exception as e:
            print(f"Failed to convert {heic_file}: {e}")

if __name__ == "__main__":
    folder = input("Enter the folder path containing HEIC images: ").strip()
    convert_heic_to_png(folder)
