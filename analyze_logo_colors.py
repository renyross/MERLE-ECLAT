from PIL import Image
from collections import Counter
import sys

def get_dominant_colors(image_path, num_colors=5):
    try:
        image = Image.open(image_path)
        image = image.convert('RGBA') # Preserve Alpha
        # image = image.resize((150, 150)) # Keep original or reasonable size to miss less detail
        image.thumbnail((200, 200))
        
        pixels = list(image.getdata())
        
        # Filter out transparent pixels
        opaque_pixels = [p for p in pixels if p[3] > 10] # minimal alpha
        
        if not opaque_pixels:
            print("Image appears to be fully transparent.")
            return

        # Count all opaque colors
        counts = Counter(opaque_pixels)
        dominant = counts.most_common(num_colors)
        
        print(f"Dominant Opaque colors in {image_path}:")
        for color, count in dominant:
            hex_color = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
            print(f"- {hex_color} (RGB: {color[:3]}) - Alpha: {color[3]}")
            
        # Try to find "Chromatic" colors (saturation > threshold)
        import colorsys
        chromatic = []
        for p in opaque_pixels:
            r, g, b = p[0]/255.0, p[1]/255.0, p[2]/255.0
            h, l, s = colorsys.rgb_to_hls(r, g, b)
            if s > 0.1 and l > 0.1 and l < 0.9: # Saturated and not too black/white
                chromatic.append(p)
                
        if chromatic:
            chrom_counts = Counter(chromatic)
            dom_chrom = chrom_counts.most_common(5)
            print(f"\nDominant Chromatic colors:")
            for color, count in dom_chrom:
                hex_color = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
                print(f"- {hex_color} (RGB: {color[:3]})")
        else:
            print("\nNo significant chromatic colors found (Monochrome).")

    except Exception as e:
        print(f"Error analyzing image: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_dominant_colors(sys.argv[1])
    else:
        print("Usage: python analyze_logo.py <image_path>")
