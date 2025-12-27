
import re

file_path = '/Users/renelrosene/Desktop/MERLE ECLAT/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find the overlay and handle start
# We capture the div and the whitespace up to the span
pattern = r'(<div class="ugc-overlay">\s*)<span class="ugc-handle">'

# Replacement: group 1 + the icon + the span
replacement = r'\1<i class="ph ph-instagram-logo" style="margin-right: 0.5rem; font-size: 1.2rem;"></i>\n                            <span class="ugc-handle">'

# Use re.sub to replace
new_content, count = re.subn(pattern, replacement, content)

print(f"Replaced {count} occurrences.")

if count > 0:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
