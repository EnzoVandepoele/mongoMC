#!/bin/bash

echo "⏳ Attente du démarrage de MongoDB..."
until mongosh --eval "db.adminCommand('ping')" > /dev/null 2>&1; do
  sleep 1
done

echo "✅ Mongo est prêt. Importation des données..."
mongoimport --db itemsDB --collection itemBlock --file /data/item_data.json --jsonArray

echo "✅ Import terminé"