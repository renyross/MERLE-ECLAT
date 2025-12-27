# Cahier d’intégration WooCommerce - Merle Éclat

Ce document détaille la stratégie technique pour porter le design "Merle Éclat" (HTML/CSS/JS) vers un environnement WordPress + WooCommerce complet.

## 1. Architecture du Thème (Theme Hierarchy)

Nous allons créer un thème sur mesure basé sur la structure actuelle.

| Fichier HTML Actuel | Template WordPress Cible | Description |
| :--- | :--- | :--- |
| **Global** | `functions.php` | Configuration, Enqueue scripts/styles, Support Woo. |
| **Global** | `header.php` | `<header>`, Nav, Meta tags. |
| **Global** | `footer.php` | `<footer>`, Scripts JS. |
| `index.html` | `front-page.php` | Page d'accueil. Sections gérées via ACF ou Gutenberg Blocks. |
| `shop.html` | `archive-product.php` | Grille produits, filtres (Sidebar), et Pagination. |
| `product.html` | `single-product.php` | Fiche produit détaillée, Galerie, Ajout panier, Cross-sell. |
| `blog.html` | `home.php` / `archive.php` | Liste des articles de blog. |
| `article.html` (théorique) | `single.php` | Article de blog individuel. |
| `contact.html` | `page-contact.php` | Template de page spécifique avec formulaire (Contact Form 7). |
| - | `woocommerce.php` | Fallback pour les pages Woo génériques. |

## 2. Gestion des Assets (CSS/JS) et Design

L'objectif est de conserver 100% du design "Antigravity".

### 2.1 Styles (CSS)
*   **Action:** Enqueue du fichier `style.css` existant dans `wp_enqueue_scripts`.
*   **WooCommerce Styles:** Désactiver les styles par défaut de WooCommerce pour éviter les conflits (`add_filter( 'woocommerce_enqueue_styles', '__return_false' );`), OU surcharger massivement.
*   **Adaptation:** Les classes CSS de WooCommerce (ex: `.woocommerce-loop-product__title`) devront être ciblées dans `style.css` pour correspondre aux styles actuels (ex: `.product-card h3`).

### 2.2 Scripts (JS)
*   **Action:** Enqueue `main.js`.
*   **Adaptation AJAX:** Le script JS actuel pour le panier (`initCartCounter`) doit être modifié pour écouter les événements jQuery de WooCommerce (`$( document.body ).on( 'added_to_cart' ... )`) afin de mettre à jour le compteur dynamiquement sans rechargement.

## 3. Structure des Données E-commerce

### 3.1 Taxonomies (Catégories)
Création des catégories correspondant à la navigation :
*   **Cheveux Naturels** (Slug: `naturel-prestige`)
*   **Cheveux Synthétiques** (Slug: `synthetique-premium`)
*   **Accessoires & Soins** (Slug: `accessoires`)
    *   *Sous-cat:* Brosses, Bonnets...

### 3.2 Attributs Produits (Global Attributes)
Pour gérer les variations (Variable Products) :
*   **Longueur:** 10", 12", 14", 16", 18", 20", 22", 24".
*   **Texture:** Lisse, Ondulé (Body Wave), Bouclé (Deep Wave), Kinky.
*   **Couleur:** Noir Naturel (1B), Chocolat, Bordeaux, Platine, Mèches (Highlight).
*   **Densité:** 150%, 180% (Si applicable).

### 3.3 Champs Personnalisés (ACF Pro Recommandé)
Pour rendre la Home et les Produits éditables :
*   **Home Hero:** Répéteur pour les Slides (Image, Titre, Lien).
*   **Home Reassurance:** Champs Texte/Icône.
*   **Produit:** Champs pour "Guide des tailles" (Popup), Vidéo produit (si hors galerie), et "Conseil d'expert".

## 4. Fonctionnalités Clés à Migrer

### 4.1 Header & Navigation
*   **Menu:** Utiliser `wp_nav_menu()`. Pour le Mega Menu, utiliser un plugin comme "Max Mega Menu" OU coder un Walker personnalisé qui reproduit la structure HTML `div.mega-menu` existante.
*   **Panier:** Le lien panier dans le header doit ouvrir le "Mini-Cart" latéral.

### 4.2 Le Mini-Cart (Panier Latéral)
*   WooCommerce n'a pas de mini-cart latéral par défaut.
*   **Solution:** Coder un template partiel `cart-panel.php` qui est chargé via AJAX, ou utiliser un plugin léger comme "Smart Floating Cart" et le styliser avec votre CSS existant.

### 4.3 Fiche Produit (`single-product.php`)
*   **Galerie:** Utiliser `add_theme_support( 'wc-product-gallery-zoom' );`, `wc-product-gallery-lightbox`, `wc-product-gallery-slider`.
*   **Bouton Ajout:** Styliser `.single_add_to_cart_button` avec la classe `.btn-primary`.
*   **Onglets:** Description, Informations Complémentaires, Avis. Styliser `.woocommerce-tabs`.

## 5. Checklist Migration & SEO

1.  **Installation:** WP + WooCommerce + ACF.
2.  **Import:** Créer les 3 produits phares manuellement pour caler le design.
3.  **Permaliens:** Régler sur `/boutique/` et `/produit/` pour le SEO fr.
4.  **URLs:** Redirections 301 des anciennes URLs `.html` vers les nouvelles URLs WP (ex: `product-soin.html` -> `/produit/serum-eclat/`).
5.  **Optimisation:** Installer un plugin de cache (WP Rocket) et d'optimisation d'images (Imagify/WebP Express) pour maintenir les scores Web Vitals.

## 6. Exemple de Code (functions.php start)

```php
function merle_eclat_scripts() {
    // Styles
    wp_enqueue_style( 'merle-style', get_template_directory_uri() . '/assets/css/style.css', array(), '1.0' );
    
    // Scripts
    wp_enqueue_script( 'merle-main', get_template_directory_uri() . '/assets/js/main.js', array('jquery'), '1.0', true );
}
add_action( 'wp_enqueue_scripts', 'merle_eclat_scripts' );

function mytheme_add_woocommerce_support() {
    add_theme_support( 'woocommerce' );
    add_theme_support( 'wc-product-gallery-zoom' );
    add_theme_support( 'wc-product-gallery-lightbox' );
    add_theme_support( 'wc-product-gallery-slider' );
}
add_action( 'after_setup_theme', 'mytheme_add_woocommerce_support' );
```
