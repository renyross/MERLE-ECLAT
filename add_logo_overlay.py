from PIL import Image

def add_logo_to_image(image_path, logo_path, output_path, position="bottom-right", scale=0.2, margin=20):
    try:
        img = Image.open(image_path).convert("RGBA")
        logo = Image.open(logo_path).convert("RGBA")
        
        # Calculate new logo size
        img_w, img_h = img.size
        logo_w, logo_h = logo.size
        
        new_logo_w = int(img_w * scale)
        aspect_ratio = logo_h / logo_w
        new_logo_h = int(new_logo_w * aspect_ratio)
        
        logo = logo.resize((new_logo_w, new_logo_h), Image.Resampling.LANCZOS)
        
        # Calculate position
        if position == "bottom-right":
            x = img_w - new_logo_w - margin
            y = img_h - new_logo_h - margin
        elif position == "top-right":
            x = img_w - new_logo_w - margin
            y = margin
        elif position == "top-left":
            x = margin
            y = margin
        elif position == "bottom-left":
            x = margin
            y = img_h - new_logo_h - margin
        elif position == "center":
            x = (img_w - new_logo_w) // 2
            y = (img_h - new_logo_h) // 2
            
        # Paste logo
        img.paste(logo, (x, y), logo)
        
        # Save
        if output_path.endswith('.jpg'):
            img = img.convert("RGB")
        img.save(output_path)
        print(f"Added logo to {output_path}")
        
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

# Apply to accessory images
# Based on grep, the image is 'assets/images/collection-accessories-new.png'
# And 'circle-accessories-branded.png'

# Also check if we need to apply to unique accessory images if they existed (bonnet, brush, etc)
# But currently shop.html uses collection-accessories-new.png for both.

images_to_brand = [
    'assets/images/collection-accessories-new.png',
    'assets/images/circle-accessories-branded.png'
]

logo_file = 'assets/images/logo.png' 

for img_file in images_to_brand:
    add_logo_to_image(img_file, logo_file, img_file, position="bottom-right", scale=0.25)
