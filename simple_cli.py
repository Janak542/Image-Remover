import argparse
from rembg import remove
from PIL import Image
from pathlib import Path

def remove_background_cli(input_path: str, output_path: str):
    """Removes the background from an image and saves the result."""
    input_file = Path(input_path)
    output_file = Path(output_path)
    
    if not input_file.exists():
        print(f"Error: Input file not found at {input_path}")
        return

    print(f"Processing {input_file.name}...")
    
    # Open input image
    input_img = Image.open(input_file)
    
    # Remove background
    output_img = remove(input_img)
    
    # Save output image (PNG preserves transparency)
    output_img.save(output_file)
    print(f"Successfully saved background-removed image to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image Background Remover using rembg.")
    parser.add_argument("input_image", help="Path to the input image file.")
    parser.add_argument("output_image", help="Path to save the output image (e.g., output.png).")
    
    args = parser.parse_args()
    remove_background_cli(args.input_image, args.output_image)