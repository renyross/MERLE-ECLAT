import os
import shutil

# Mapping from brain files to project files
# Syntax: (brain_dir_id, brain_file_prefix) -> target_rel_path
MAPPING = {
    # Main Sections
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'hero_banner_wig'): 'hero-bg.png',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'hero_ref_1_duo'): 'hero-ref-1.png',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'collection_natural_hair'): 'circle-naturel.png',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'collection_synthetic_hair'): 'circle-synthetic.png',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'collection_accessories'): 'circle-accessories-branded.png',
    
    # Products (Original)
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'product_wig_long_wavy'): 'product-1.png',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'product_wig_bob_red'): 'product-2.png',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'product_wig_curly_afro'): 'product-3.png',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'product_wig_straight_blonde'): 'product-4.png',
    
    # Products (V2 / Hero Slides)
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'hero_banner_2_blonde'): 'product-1-v2.png',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'hero_banner_3_red'): 'product-2-v2.png',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'hero_banner_4_brunette'): 'product-4-v2.png',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'hero_banner_5_curly'): 'product-3-v2.png',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'hero_ref_1_duo'): 'circle-best-sellers-duo.png', 
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'hero_ref_2'): 'hero-slide-3.png',
    ('61cf24ef-9cb4-4224-a40a-695473fd1bb4', 'collection_accessories_new'): 'collection-accessories-new.png',
    
    # UGC
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_1_'): 'ugc-1.png',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_2_'): 'ugc-2.png',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_3_'): 'ugc-3.png',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_4_'): 'ugc-4.png',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_5_'): 'ugc-5.png',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_6_'): 'ugc-6.png',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_7_'): 'ugc-7.png',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_8_'): 'ugc-8.png',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_9_'): 'ugc-9.png',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_10_'): 'ugc-10.png',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_11_'): 'ugc-11.png',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'ugc_social_12_'): 'ugc-12.png',

    # Transformation
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'transformation_before'): 'transformation-before.png',
    ('fae0c564-ad14-4dfa-9ebf-dcb1187a4ca2', 'transformation_after_aligned'): 'transformation-after.png',

    # Logo
    ('bdc9360d-ba06-4085-9fc9-9032e7d02b08', 'merle_eclat_logo_icon'): 'logo.png',
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
            target_path = os.path.join(TARGET_BASE, target_name)
            shutil.copy2(source, target_path)
            print(f"Restored {target_name} from {source}")
        except Exception as e:
            print(f"Error restoring {target_name}: {e}")
    else:
        print(f"Could not find source for {target_name} (Search: {brain_id}/{prefix})")

print("\nDone.")
