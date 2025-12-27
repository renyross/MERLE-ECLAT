# Plan de Maillage Interne & Architecture SEO - Merle Éclat

## 1. Structure en Silos Sémantiques

L'architecture est organisée pour maximiser la pertinence thématique (Topical Authority). Chaque univers agit comme un "silo" étanche qui renforce ses propres pages avant de lier vers les autres.

### Silo A : L'Excellence Naturelle (Cheveux Naturels)
*Cœur de cible : Clients cherchant le luxe, la durabilité et le réalisme.*
1.  **Page Catégorie Mère :** `shop.html?category=naturel` (Titre : "Perruques Cheveux Naturels - Collection Prestige")
2.  **Sous-Catégories (Filtres/Pages dédiées) :**
    *   *Par Longueur :* 10-12” (Carrés), 14-16” (Mi-longs), 18-20” (Longs), 22-24” (Très Longs).
    *   *Par Style :* Lisse (Straight), Ondulé (Body Wave), Bouclé (Deep Wave/Kinky).
3.  **Produits Phares :**
    *   "L'Ondulée Noire" (Ref: Natural-Wavy-22)
    *   "Afro Kinky Volume" (Ref: Natural-Kinky-14)

### Silo B : Le Style Premium (Cheveux Synthétiques)
*Cœur de cible : Clients cherchant le style, la facilité, le changement fréquent.*
1.  **Page Catégorie Mère :** `shop.html?category=synthetique` (Titre : "Perruques Synthétiques Premium - Fibres Haute Température")
2.  **Sous-Catégories :**
    *   *Par Couleur :* Naturelles, Colorées (Bordeaux, Platine, Mèches).
3.  **Produits Phares :**
    *   "Le Carré Bordeaux" (Ref: Synth-Bob-Red)
    *   "Lisse Platine" (Ref: Synth-Platinium-24)

### Silo C : L'Atelier Soin & Accessoires
*Silo de soutien pour augmenter le Panier Moyen et la Rétention.*
1.  **Page Catégorie Mère :** `shop.html?category=accessoires`
2.  **Produits :**
    *   Brosse Démêlante (Lien vers entretien perruques)
    *   Bonnet en Satin (Lien vers protection nuit)
    *   Sérum Brillance (Lien vers finition)

---

## 2. Stratégie de Transfert d'Autorité (PageRank Sculpting)

### Depuis la Page d'Accueil (`index.html`)
La "Home" possède le plus d'autorité. Elle doit la distribuer stratégiquement :
*   **Hero Section :** 1 lien fort vers la collection principale ("Découvrir la Collection Prestige" -> `shop.html?category=naturel`).
*   **Best Sellers :** Liens directs vers les 3 produits les plus vendus (Taux de conversion max).
*   **Footer :** Liens vers les catégories mères, pas vers les produits individuels (pour ne pas diluer).

### Maillage Transversal (Cross-Linking) Contextuel
*Lier les silos entre eux de manière logique pour l'utilisateur, pas pour le robot.*

| Page Source | Page Cible | Ancre Recommandée (Anchor Text) | Rationale UX/SEO |
| :--- | :--- | :--- | :--- |
| **Fiche Produit Perruque** (ex: L'Ondulée) | **Produit Accessoire** (ex: Brosse) | "L'outil indispensable pour ce style" | Cross-sell naturel, augmente le panier moyen. |
| **Fiche Produit Perruque** (ex: L'Ondulée) | **Produit Accessoire** (ex: Bonnet) | "Protéger votre chevelure la nuit" | Conseil d'expert, réassurance. |
| **Article Blog** ("Comment laver sa perruque") | **Produit Soin** (ex: Sérum/Shampoing) | "Utiliser notre sérum éclat spécifique" | Répond à l'intention "Comment faire" par "Avec quoi". |
| **Article Blog** ("Choisir sa longueur") | **Catégorie Naturel** | "Voir nos modèles longs (22-24 pouces)" | Guide l'utilisateur informatif vers l'achat. |
| **Page Accessoires** | **Catégorie Synthétique** | "Sublimez vos modèles synthétiques" | Rappel du produit principal. |

---

## 3. Plan d'Ancres Optimisées

Éviter la sur-optimisation tout en restant descriptif.

*   ✅ **OUI :**
    *   "Choisir ma perruque naturelle"
    *   "Voir les accessoires de pose"
    *   "Découvrir la gamme Kinky"
    *   "Entretenir mes ondulations"
*   ❌ **NON :**
    *   "Cliquez ici" (Vide de sens)
    *   "Perruque pas cher" (Dégrade l'image de marque)
    *   "En savoir plus" (Trop générique, sauf pour boutons secondaires)

---

## 4. Recommandations Techniques & UX

### Limitation des Liens Sortants
*   **Menu Principal (Mega Menu) :** Limiter aux entrées essentielles (Naturel, Synthétique, Accessoires, Blog). Éviter de lister *tous* les produits dans le menu.
*   **Produits Apparentés :** Limiter à 3 ou 4 suggestions en bas de page produit. Trop de choix tue la conversion (Paradoxe du choix).

### Fil d'Ariane (Breadcrumbs)
Implémenter systématiquement un fil d'ariane pour renforcer la structure hiérarchique :
*   `Accueil > Boutique > Cheveux Naturels > L'Ondulée Noire`
*   Cela crée automatiquement des liens parents et renforce le silo.

### Blog comme Portes d'Entrée (Inbound Marketing)
Créer des articles qui répondent aux questions "Longue traîne" (Long Tail Keywords) :
1.  *Article :* "Synthétique vs Naturel : Que choisir pour une première perruque ?" -> Lien vers les deux catégories.
2.  *Article :* "5 astuces pour garder sa perruque brillante" -> Lien vers le Sérum et la Brosse.

---

## 5. Action Plan (Mise en œuvre immédiate)

1.  **Mise à jour du Footer :** Vérifier que les liens pointent vers les catégories principales (`shop.html?category=...`) et non des pages orphelines.
2.  **Optimisation Fiches Produits :** Ajouter un bloc "Complétez votre routine" avec des liens manuels vers les accessoires pertinents (Brosse, Bonnet).
3.  **Blog :** S'assurer que chaque article contient au moins 1 lien vers une Collection et 1 lien vers un Produit spécifique.
