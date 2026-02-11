import json

# Load the data
with open('/Users/abenu/Downloads/Forecast/chinese/hanja_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Read the HTML template
with open('/Users/abenu/Downloads/Forecast/chinese/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# New placeholder matching the updated index.html
placeholder = 'const HANJA_DATA = {\n            "8급": [],\n            "7급": [],\n            "6급": []\n        };'

# Replace the data placeholder
data_js = f"const HANJA_DATA = {json.dumps(data, ensure_ascii=False)};"
html = html.replace(placeholder, data_js)

# Write back to index.html
with open('/Users/abenu/Downloads/Forecast/chinese/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Data successfully embedded into index.html")
