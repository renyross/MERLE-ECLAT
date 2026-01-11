
import glob
import os

# HTML for the marquee
marquee_html = """
    <!-- Announcement Bar -->
    <div class="announcement-bar">
        <div class="marquee-track">
            <div class="marquee-content">
                <span>LIVRAISON GRATUITE EN FRANCE ET EN EUROPE DÈS 80€ D'ACHAT &nbsp;&bull;&nbsp; </span>
                <span>LIVRAISON GRATUITE EN FRANCE ET EN EUROPE DÈS 80€ D'ACHAT &nbsp;&bull;&nbsp; </span>
                <span>LIVRAISON GRATUITE EN FRANCE ET EN EUROPE DÈS 80€ D'ACHAT &nbsp;&bull;&nbsp; </span>
                <span>LIVRAISON GRATUITE EN FRANCE ET EN EUROPE DÈS 80€ D'ACHAT &nbsp;&bull;&nbsp; </span>
            </div>
            <!-- Duplicate for infinite scroll -->
            <div class="marquee-content">
                <span>LIVRAISON GRATUITE EN FRANCE ET EN EUROPE DÈS 80€ D'ACHAT &nbsp;&bull;&nbsp; </span>
                <span>LIVRAISON GRATUITE EN FRANCE ET EN EUROPE DÈS 80€ D'ACHAT &nbsp;&bull;&nbsp; </span>
                <span>LIVRAISON GRATUITE EN FRANCE ET EN EUROPE DÈS 80€ D'ACHAT &nbsp;&bull;&nbsp; </span>
                <span>LIVRAISON GRATUITE EN FRANCE ET EN EUROPE DÈS 80€ D'ACHAT &nbsp;&bull;&nbsp; </span>
            </div>
        </div>
    </div>
"""

files = glob.glob("/Users/renelrosene/Desktop/MERLE ECLAT/*.html")

for file_path in files:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check if already added
        if "announcement-bar" in content:
            print(f"Skipping {os.path.basename(file_path)}: already has announcement bar")
            continue

        # Inject after <body>
        if "<body>" in content:
            new_content = content.replace("<body>", f"<body>{marquee_html}")
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Added announcement bar to {os.path.basename(file_path)}")
        else:
            print(f"Skipping {os.path.basename(file_path)}: <body> tag not found")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
