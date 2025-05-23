import json
import sys

# Vérifie les arguments
if len(sys.argv) != 3:
    print("Utilisation : python convert_json_to_array.py entrée.json sortie.json")
    sys.exit(1)

# Fichiers
fichier_entree = sys.argv[1]
fichier_sortie = sys.argv[2]

# Conversion
with open(fichier_entree, 'r', encoding='utf-8') as f:
    data = json.load(f)

documents = []
for nom, contenu in data.items():
    contenu["_id"] = nom  # Utilise la clé comme ID
    documents.append(contenu)

with open(fichier_sortie, 'w', encoding='utf-8') as f:
    json.dump(documents, f, indent=2, ensure_ascii=False)

print(f"✅ Fichier converti et sauvegardé dans : {fichier_sortie}")
