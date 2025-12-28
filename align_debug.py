from PIL import Image

def create_debug_image():
    try:
        img_before = Image.open('assets/images/transformation-before.png').convert('RGBA')
        img_after = Image.open('assets/images/transformation-after.png').convert('RGBA')

        # Resize to match
        width = min(img_before.width, img_after.width)
        height = min(img_before.height, img_after.height)
        
        img_before = img_before.resize((width, height))
        img_after = img_after.resize((width, height))

        # Blend
        blended = Image.blend(img_before.convert('RGB'), img_after.convert('RGB'), 0.5)
        blended.save('assets/images/alignment_debug.jpg')
        print("Created alignment_debug.jpg")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_debug_image()
