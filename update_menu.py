
import os
import re

# The new navigation menu HTML content
new_nav_content = """<nav class="nav-links">
                <!-- 1. Nos Perruques (Merged) -->
                <div class="nav-item">
                    <a href="shop.html" class="nav-link">NOS PERRUQUES <i class="ph ph-caret-down"
                            style="font-size: 0.8rem;"></i></a>
                    <div class="mega-menu">
                        <!-- Column 1: Par Collection -->
                        <div class="mega-column">
                            <h4>Par Type</h4>
                            <ul>
                                <li><a href="shop.html?category=naturel" style="font-weight: 600;">Cheveux Naturels</a>
                                </li>
                                <li><a href="shop.html?category=synthetique" style="font-weight: 600;">Cheveux
                                        Synthétiques</a></li>
                                <li><a href="shop.html?style=closures" style="font-weight: 600;">Closures / Frontals</a></li>
                            </ul>
                        </div>

                        <!-- Column 2: Par Style -->
                        <div class="mega-column">
                            <h4>Par Style</h4>
                            <ul>
                                <li><a href="shop.html?style=lisse">Lisse / Straight</a></li>
                                <li><a href="shop.html?style=boucle">Bouclé / Curly</a></li>
                                <li><a href="shop.html?style=ondule">Ondulé / Wavy</a></li>
                                <li><a href="shop.html?style=afro">Afro / Kinky</a></li>
                            </ul>
                        </div>

                        <!-- Column 3: Par Couleur -->
                        <div class="mega-column">
                            <h4>Par Couleur</h4>
                            <ul>
                                <li><a href="shop.html?color=noir"><span class="color-swatch"
                                            style="background-color: #000000;"></span> Noir</a></li>
                                <li><a href="shop.html?color=brun"><span class="color-swatch"
                                            style="background-color: #4b3621;"></span> Brun</a></li>
                                <li><a href="shop.html?color=blond"><span class="color-swatch"
                                            style="background-color: #f0e68c;"></span> Blond</a></li>
                                <li><a href="shop.html?color=colore"><span class="color-swatch"
                                            style="background: linear-gradient(to right, #4b3621, #f0e68c);"></span>
                                        Méché / Ombré</a></li>
                            </ul>
                        </div>

                        <!-- Column 4: Par Longueur -->
                        <div class="mega-column">
                            <h4>Par Longueur</h4>
                            <ul>
                                <li><a href="shop.html?length=16">16″ pouces</a></li>
                                <li><a href="shop.html?length=18">18″ pouces</a></li>
                                <li><a href="shop.html?length=20-22">20″–22″ pouces</a></li>
                                <li><a href="shop.html?length=24">24″ pouces</a></li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- 3. Accessoires & Soins -->
                <div class="nav-item">
                    <a href="shop.html" class="nav-link">Accessoires & Soins <i class="ph ph-caret-down"
                            style="font-size: 0.8rem;"></i></a>
                    <div class="mega-menu mega-menu-small">
                        <div class="mega-column">
                            <ul style="margin-top: 0.5rem;">
                                <li><a href="product-bonnet.html">Bonnets et filets</a></li>
                                <li><a href="product-soin.html">Produits d’entretien</a>
                                </li>
                                <li><a href="product-brosse.html">Peignes et brosses</a></li>
                                <li><a href="shop.html?category=accessoires&type=support">Porte-Perruque & Support</a></li>
                                <li><a href="shop.html?category=accessoires&type=foulard">Foulard</a></li>
                                <li><a href="shop.html?category=accessoires&type=turban">Turban</a></li>
                                <li><a href="shop.html?category=accessoires"
                                        style="font-weight: 600; text-decoration: underline;">Voir tout les
                                        accessoires</a></li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- 4. Best-Sellers (Direct Link) -->
                <div class="nav-item">
                    <a href="shop.html?category=best-sellers" class="nav-link"
                        style="color: var(--color-secondary); font-weight: 600;">Best-Sellers</a>
                </div>

                <!-- 5. Blog -->
                <div class="nav-item"><a href="blog.html" class="nav-link">Blog</a></div>
            </nav>"""

# List of files to update
files_to_update = [
    "shop.html",
    "product.html",
    "product-bonnet.html",
    "product-brosse.html",
    "product-soin.html",
    "blog.html",
    "contact.html"
]

base_path = "/Users/renelrosene/Desktop/MERLE ECLAT/"

for file_name in files_to_update:
    file_path = os.path.join(base_path, file_name)
    if not os.path.exists(file_path):
        print(f"Skipping {file_name}: File not found.")
        continue

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to find the nav block
        # Looking for <nav class="nav-links"> ... </nav>
        # Utilizing lookahead to ensure valid replacement
        pattern = re.compile(r'<nav class="nav-links">.*?</nav>', re.DOTALL)
        
        if pattern.search(content):
            new_content = pattern.sub(new_nav_content, content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file_name}")
        else:
            print(f"Warning: Could not find nav block in {file_name}")

    except Exception as e:
        print(f"Error processing {file_name}: {e}")
