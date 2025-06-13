import json

with open('mongo/item_data.json', 'r', encoding='utf-8') as infile:
    data = json.load(infile)

with open('item_data_clean.ndjson', 'w', encoding='utf-8') as outfile:
    for entry in data:
        entry.pop('_id', None)  # Supprime le champ _id s'il existe
        json.dump(entry, outfile)
        outfile.write('\n')
