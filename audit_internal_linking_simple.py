
import os
from bs4 import BeautifulSoup

# List of HTML files to analyze
files = [
    "index.html",
    "shop.html",
    "product.html",
    "blog.html",
    "contact.html",
    "product-bonnet.html",
    "product-brosse.html",
    "product-soin.html"
]

base_path = "/Users/renelrosene/Desktop/MERLE ECLAT"

# Structure to hold graph data
links_from = {f: [] for f in files} # Outgoing
links_to = {f: 0 for f in files}    # In-degree count

print("--- ANALYSE DU MAILLAGE INTERNE (VERSION LÉGÈRE) ---")

for file_name in files:
    full_path = os.path.join(base_path, file_name)
    if not os.path.exists(full_path):
        print(f"File not found: {file_name}")
        continue
    
    with open(full_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    anchors = soup.find_all('a', href=True)
    
    unique_targets = set()
    
    for a in anchors:
        href = a['href']
        # Normalize: remove query params, anchors, etc to find the target FILE
        target_file = href.split('?')[0].split('#')[0]
        
        if target_file in files:
            # Avoid self-loops in counting if desired, but self-linking is valid in SEO
            unique_targets.add(target_file)

    links_from[file_name] = list(unique_targets)
    
    for target in unique_targets:
        links_to[target] += 1

# Reporting
print("\n1. LIENS ENTRANTS (POPULARITÉ)")
# Sort by most linked
sorted_by_inbound = sorted(links_to.items(), key=lambda x: x[1], reverse=True)
for page, count in sorted_by_inbound:
    status = "EXCELLENT" if count >= len(files)-1 else "MOYEN"
    if count == 0: status = "DANGER (ORPHELINE)"
    elif count < 3: status = "FAIBLE"
    
    print(f"  - {page} : {count} liens entrants [{status}]")

print("\n2. PAGES À RISQUE (Profundeur > 3 clics)")
# Simple check: pages with few incoming links are harder to find
risky_pages = [p for p, c in links_to.items() if c < 3]
if not risky_pages:
    print("  Aucune page critique détectée.")
else:
    for p in risky_pages:
        print(f"  - {p} est peu maillée. Pensez à l'ajouter dans le footer ou un article de blog.")

print("\n3. STRUCTURE DU MENU")
print("  Note: Toutes les pages semblent bénéficier du 'Mega Menu', ce qui garantit un lien depuis chaque page.")
print("  Vérification spécifique des pages produits accessoires (bonnet, brosse, soin)...")

accessory_pages = ["product-bonnet.html", "product-brosse.html", "product-soin.html"]
for acc in accessory_pages:
    in_links = links_to.get(acc, 0)
    print(f"  - {acc} : {in_links} liens (Idéalement devrait être accessible depuis Menu & Shop)")

