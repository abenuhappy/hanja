import csv
import json

def parse_hanja_csv(filepath):
    data = {
        "8급": [],
        "7급": [],
        "6급": []
    }
    
    # Use utf-8-sig to handle potential BOM
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Normalize keys just in case
            level = row.get('급수', row.get('\ufeff급수', '')).strip()
            hanja = row.get('한자', '').strip()
            huenem = row.get('훈음', '').strip()
            
            if not level or not hanja:
                continue
                
            parts = huenem.split()
            if len(parts) >= 2:
                meaning = " ".join(parts[:-1])
                sound = parts[-1]
            else:
                meaning = huenem
                sound = ""
                
            item = {
                "hanja": hanja,
                "meaning": meaning,
                "sound": sound
            }
            
            if level in data:
                data[level].append(item)
            else:
                # Handle unexpected levels if any
                if level not in data:
                    data[level] = []
                data[level].append(item)
                
    return data

if __name__ == "__main__":
    hanja_data = parse_hanja_csv('/Users/abenu/Downloads/Forecast/chinese/hanja.csv')
    
    with open('/Users/abenu/Downloads/Forecast/chinese/hanja_data.json', 'w', encoding='utf-8') as f:
        json.dump(hanja_data, f, ensure_ascii=False, indent=2)
    
    for level, items in hanja_data.items():
        print(f"Level {level}: {len(items)} items")
