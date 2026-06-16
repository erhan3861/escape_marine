import json

def main():
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
    texts_list = data.get("Texts", [])
    extracted = []
    
    print(f"Total Text elements in JSON: {len(texts_list)}")
    for idx, item in enumerate(texts_list):
        text_msg = item.get("TextMessage", "")
        name = item.get("Name", "")
        slide_id = item.get("IdSlide", "")
        text_id = item.get("Id", "")
        
        if text_msg:
            extracted.append({
                "index": idx,
                "id": text_id,
                "name": name,
                "slide_id": slide_id,
                "text_message": text_msg
            })
            
    print(f"Extracted {len(extracted)} non-empty TextMessage elements.")
    
    with open("extracted_text_messages.json", "w", encoding="utf-8") as f:
        json.dump(extracted, f, indent=2, ensure_ascii=False)
        
    # Print sample
    for item in extracted[:10]:
        print(f"\n- Index {item['index']} ({item['name']}): {item['text_message']}")

if __name__ == "__main__":
    main()
