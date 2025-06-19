from PIL import Image
import os

def convert_image(file_path, out_format="JPEG"):
    img = Image.open(file_path)
    base, ext = os.path.splitext(file_path)
    new_file = f"{base}.{out_format.lower()}"
    img.save(new_file, out_format)
    print(f"Saved {new_file}")

def main():
    print("Image Converter")
    file_path = input("Enter image file path: ")
    out_format = input("Convert to format (e.g., JPEG, PNG): ").upper()
    convert_image(file_path, out_format)

if __name__ == "__main__":
    main()