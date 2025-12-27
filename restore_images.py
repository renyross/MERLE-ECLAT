import os
from PIL import Image

# Mapping from brain files to project files
# Syntax: (brain_dir_id, brain_file_prefix) -> target_rel_path
MAPPING = {
    # Main Sections
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'hero_banner_wig'): 'hero-bg.webp',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'hero_ref_1_duo'): 'hero-ref-1.webp',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'collection_natural_hair'): 'circle-naturel.webp',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'collection_synthetic_hair'): 'circle-synthetic.webp',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'collection_accessories'): 'circle-accessories-branded.webp',
    
    # Products (Original)
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'product_wig_long_wavy'): 'product-1.webp',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'product_wig_bob_red'): 'product-2.webp',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'product_wig_curly_afro'): 'product-3.webp',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'product_wig_straight_blonde'): 'product-4.webp',
    
    # Products (V2 / Hero Slides)
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'hero_banner_2_blonde'): 'product-1-v2.webp',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'hero_banner_3_red'): 'product-2-v2.webp',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'hero_banner_4_brunette'): 'product-4-v2.webp',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'hero_banner_5_curly'): 'product-3-v2.webp',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'hero_ref_1_duo'): 'circle-best-sellers-duo.webp', 
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'hero_ref_2'): 'hero-slide-3.webp',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'collection_accessories_new'): 'collection-accessories-new.webp',
    
    # UGC
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_1_'): 'ugc-1.webp',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_2_'): 'ugc-2.webp',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_3_'): 'ugc-3.webp',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_4_'): 'ugc-4.webp',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_5_'): 'ugc-5.webp',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_6_'): 'ugc-6.webp',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_7_'): 'ugc-7.webp',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_8_'): 'ugc-8.webp',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_9_'): 'ugc-9.webp',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_10_'): 'ugc-10.webp',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_11_'): 'ugc-11.webp',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_12_'): 'ugc-12.webp',

    # Transformation
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'transformation_before'): 'transformation-before.webp',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'transformation_after_aligned'): 'transformation-after.webp',

    # Logo
    ('bdc9360d-ba06-4085-9fc9-9032e7d02b08', 'merle_eclat_logo_icon'): 'logo.webp',
}

BRAIN_BASE = '/Users/renelrosene/.gemini/antigravity/brain/'
TARGET_BASE = '/Users/renelrosene/Desktop/MERLE ECLAT/assets/images/'

if not os.path.exists(TARGET_BASE):
    os.makedirs(TARGET_BASE)

def find_file(brain_id, prefix):
    brain_dir = os.path.join(BRAIN_BASE, brain_id)
    if not os.path.exists(brain_dir):
        return None
    for f in os.listdir(brain_dir):
        if f.startswith(prefix) and (f.endswith('.png') or f.endswith('.jpg') or f.endswith('.webp')):
            return os.path.join(brain_dir, f)
    return None

for (brain_id, prefix), target_name in MAPPING.items():
    source = find_file(brain_id, prefix)
    if source:
        try:
            img = Image.open(source)
            target_path = os.path.join(TARGET_BASE, target_name)
            img.save(target_path, 'WEBP')
            print(f"Restored {target_name} from {source}")
        except Exception as e:
            print(f"Error restoring {target_name}: {e}")
    else:
        print(f"Could not find source for {target_name} (Search: {brain_id}/{prefix})")

print("\nDone.")
