
import os
from bs4 import BeautifulSoup
import networkx as nx

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
G = nx.DiGraph()

print("--- ANALYSE DU MAILLAGE INTERNE ---")

for file_name in files:
    full_path = os.path.join(base_path, file_name)
    if not os.path.exists(full_path):
        continue
    
    with open(full_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    links = soup.find_all('a', href=True)
    
    outgoing_links = []
    for link in links:
        href = link['href']
        # Filter internal links only (ignoring anchors on same page for now unless useful)
        if href and not href.startswith('http') and not href.startswith('#') and not href.startswith('mailto'):
            # Simplify href to remove query params for graph structure
            target = href.split('?')[0]
            if target in files:
                outgoing_links.append(target)
                G.add_edge(file_name, target)

    print(f"\nPAGE: {file_name}")
    print(f"  -> Nombre de liens sortants internes : {len(outgoing_links)}")
    print(f"  -> Liens vers : {set(outgoing_links)}")

print("\n--- MÉTRIQUES CLÉS ---")
# PageRank calculation (simple)
try:
    pagerank = nx.pagerank(G)
    sorted_pr = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
    print("\nScore de PageRank interne (Popularité estimée) :")
    for page, score in sorted_pr:
        print(f"  {page}: {score:.4f}")
except Exception as e:
    print("Graph calculation error:", e)

# Check for Orphan Pages
nodes = set(files)
graph_nodes = set(G.nodes())
orphans = nodes - graph_nodes
# Also check nodes with 0 in-degree
in_degrees = dict(G.in_degree())
zero_in_degree = [n for n, d in in_degrees.items() if d == 0]

print("\nPages Orphelines (Aucun lien entrant) :")
if zero_in_degree:
    for p in zero_in_degree:
        print(f"  - {p} (ATTENTION: Google ne peut pas trouver cette page facilement)")
else:
    print("  Aucune page orpheline trouvée.")

# Check for isolated loops or broken chains requires more detailed analysis, 
# but simply listing strongly connected components helps.
print("\nComposantes fortement connectées :")
scc = list(nx.strongly_connected_components(G))
for component in scc:
    print(f"  - {component}")

