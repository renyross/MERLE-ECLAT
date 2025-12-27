from PIL import Image

def add_logo_to_image(image_path, logo_path, output_path, position="center", scale=0.3, opacity=0.8):
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
        
        # Apply opacity
        if opacity < 1.0:
            datas = logo.getdata()
            newData = []
            for item in datas:
                newData.append((item[0], item[1], item[2], int(item[3] * opacity)))
            logo.putdata(newData)
            
        # Calculate position
        if position == "center":
            x = (img_w - new_logo_w) // 2
            y = (img_h - new_logo_h) // 2
            
        # Paste logo
        img.paste(logo, (x, y), logo)
        
        # Save
        img.save(output_path)
        print(f"Added centered logo to {output_path}")
        
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

# Apply to accessory images
images_to_brand = [
    'assets/images/collection-accessories-new.png',
    'assets/images/circle-accessories-branded.png'
]

logo_file = 'assets/images/logo.png' 

for img_file in images_to_brand:
    add_logo_to_image(img_file, logo_file, img_file, position="center", scale=0.35, opacity=0.9)
