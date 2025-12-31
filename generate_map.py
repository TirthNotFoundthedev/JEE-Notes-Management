import os
import json

# Configuration
DATA_DIR = "data"
OUTPUT_FILE = "manifest.json"

def generate_manifest():
    # Structure: { Category: { Notebook: [ {name: "Item1.html", type: "Item1"} ] } }
    manifest = {}

    if not os.path.exists(DATA_DIR):
        print(f"❌ Error: Folder '{DATA_DIR}' not found. Please create it.")
        return

    # Walk through Category Folders
    for category in os.listdir(DATA_DIR):
        cat_path = os.path.join(DATA_DIR, category)
        if os.path.isdir(cat_path):
            manifest[category] = {}
            
            # Walk through Notebook Folders
            for notebook in os.listdir(cat_path):
                nb_path = os.path.join(cat_path, notebook)
                if os.path.isdir(nb_path):
                    manifest[category][notebook] = []
                    
                    # Walk through Items
                    for item in os.listdir(nb_path):
                        if item.startswith('.'): continue # Skip hidden files
                        
                        # Get filename without extension
                        item_type = os.path.splitext(item)[0]
                        
                        manifest[category][notebook].append({
                            "name": item,
                            "type": item_type
                        })

    with open(OUTPUT_FILE, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"✅ Success! Scanned {len(manifest)} categories.")
    print(f"📂 Manifest saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_manifest()