
import re

file_path = '/Users/renelrosene/Desktop/MERLE ECLAT/index.html'

# Mapping of current generic handles to new diverse/realistic handles
handle_mapping = {
    "@thedailyglow": "@sarah.in.paris",
    "@parisienne_chic": "@chloe_lifestyle",
    "@drive_with_style": "@beauty_by_lina",
    "@kinky_queen": "@afro_queen_93",
    "@luxury_unboxing": "@marie_glam",
    "@event_glam": "@elise_events",
    "@city_vibes": "@julie_urban",
    "@morning_routine": "@clara_morning",
    "@texture_lover": "@natural_hair_joy",
    "@glam_mirror": "@sophie_chic",
    "@on_the_go_style": "@travel_with_nina",
    "@nature_curl": "@emma_curls"
}

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_content = content
for old, new in handle_mapping.items():
    new_content = new_content.replace(old, new)

if new_content != content:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Handles updated successfully.")
else:
    print("No handles found to update.")
