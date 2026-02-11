import re
import json

def parse_hanja_file(filepath):
    middle_900 = []
    high_900 = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_pron = ""
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Skip headers
        if "중학교" in line or "고등학교" in line:
            continue
            
        # Pronunciation header (e.g., '가')
        if len(line) <= 2 and not "(" in line:
            current_pron = line
            continue
            
        # Hanja entries
        # Format: 佳 (아름다울 가) · 假 (거짓 가)
        entries = re.findall(r'(\w)\s*\((.*?)\)', line)
        
        # Heuristic: If it's the first line after a pronunciation header, it's Middle School.
        # If it's the second line under the same header, it's High School.
        # Check if previous non-empty line was the pronunciation header.
        prev_idx = i - 1
        while prev_idx >= 0 and not lines[prev_idx].strip():
            prev_idx -= 1
            
        prev_line = lines[prev_idx].strip() if prev_idx >= 0 else ""
        
        is_middle = (prev_line == current_pron)
        
        for hanja, meaning_sound in entries:
            # meaning_sound is "아름다울 가"
            parts = meaning_sound.split()
            if len(parts) >= 2:
                meaning = " ".join(parts[:-1])
                sound = parts[-1]
            else:
                meaning = meaning_sound
                sound = ""
                
            item = {
                "hanja": hanja,
                "meaning": meaning,
                "sound": sound
            }
            
            if is_middle:
                middle_900.append(item)
            else:
                high_900.append(item)
                
    return middle_900, high_900

if __name__ == "__main__":
    middle, high = parse_hanja_file('/Users/abenu/Downloads/Forecast/chinese/한자.txt')
    data = {
        "middle": middle,
        "high": high
    }
    with open('/Users/abenu/Downloads/Forecast/chinese/hanja_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Parsed {len(middle)} middle school and {len(high)} high school characters.")
