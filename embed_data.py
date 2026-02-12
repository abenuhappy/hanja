import json
import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(base_dir, 'hanja_data.json')
html_path = os.path.join(base_dir, 'index.html')

# Load the data
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Read the HTML template
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Prepare the new data string
data_js = f"const HANJA_DATA = {json.dumps(data, ensure_ascii=False)};"

# Regex to find the existing HANJA_DATA block
# Patterns: const HANJA_DATA = { ... };
# We use re.DOTALL to match across lines if formatted
pattern = r"const\s+HANJA_DATA\s*=\s*\{.*?\};"

if re.search(pattern, html, re.DOTALL):
    html = re.sub(pattern, data_js, html, flags=re.DOTALL)
    print("Replaced existing HANJA_DATA.")
else:
    # If not found, try the old placeholder method as backup or append?
    # For now, let's assume it exists or warn.
    print("Warning: Could not find existing HANJA_DATA block. Appending to script?")
    # Fallback to the specific placeholder if relevant, but regex should catch it.
    placeholder = 'const HANJA_DATA = {\n            "8급": [],\n            "7급": [],\n            "6급": []\n        };'
    if placeholder in html:
         html = html.replace(placeholder, data_js)
         print("Replaced placeholder.")

# Write back to index.html
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Data successfully embedded into index.html")
