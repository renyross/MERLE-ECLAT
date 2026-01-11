
import os
import glob

# The block to remove (approximate content, will use simple string matching or regex)
# Since white space might vary, I'll identify it by the class and content unique combination or just specific lines if I was sure, but regex is safer for multiple files.
import re

search_pattern = re.compile(r'\s*<div class="nav-item">\s*<a href="shop.html\?category=best-sellers" class="nav-link[^"]*">Best-Sellers</a>\s*</div>', re.DOTALL)

# List of files to update
files = glob.glob("/Users/renelrosene/Desktop/MERLE ECLAT/*.html")

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if search_pattern.search(content):
            new_content = search_pattern.sub('', content)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed Best-Sellers from {os.path.basename(file_path)}")
        else:
            print(f"Best-Sellers not found in {os.path.basename(file_path)}")
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
