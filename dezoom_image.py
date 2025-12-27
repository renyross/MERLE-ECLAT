from PIL import Image
import sys

def dezoom_image(input_path, output_path, zoom_factor=0.8, y_offset_ratio=0.0, x_offset_ratio=0.0):
    try:
        img = Image.open(input_path).convert("RGBA")
        width, height = img.size
        
        # New dimensions
        new_width = int(width / zoom_factor)
        new_height = int(height / zoom_factor)
        
        # Create new background (blurred version of original or solid color)
        # For simplicity and style, let's use a scaled up version of the image, blurred, as background
        # darker to not distract
        
        bg = img.copy().resize((new_width, new_height), Image.Resampling.LANCZOS)
        # Blur the background

        try:
             # PIL 10+ might differ, but standard filter
             from PIL import ImageFilter
             bg = bg.filter(ImageFilter.GaussianBlur(radius=50))
             # Darken it
             from PIL import ImageEnhance
             enhancer = ImageEnhance.Brightness(bg)
             bg = enhancer.enhance(0.5)
        except Exception as e:
            print(f"Filter error: {e}, falling back to black")
            bg = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 255))

        # Calculate position to paste original
        # Centered default
        center_y = (new_height - height) // 2
        
        # Apply offset (ratio of new_height)
        # negative ratio moves image UP (y decreases)
        extra_y = int(new_height * y_offset_ratio)
        y_offset = center_y + extra_y
        
        center_x = (new_width - width) // 2
        extra_x = int(new_width * x_offset_ratio)
        x_offset = center_x + extra_x

        # Paste original
        bg.paste(img, (x_offset, y_offset), img)
        
        bg.save(output_path)
        print(f"Successfully saved dezoomed image to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python dezoom.py <input> <output> [zoom_factor] [y_offset_ratio] [x_offset_ratio]")
    else:
        zoom = float(sys.argv[3]) if len(sys.argv) > 3 else 0.8
        y_off = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0
        x_off = float(sys.argv[5]) if len(sys.argv) > 5 else 0.0
        dezoom_image(sys.argv[1], sys.argv[2], zoom, y_off, x_off)
