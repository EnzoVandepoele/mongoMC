#!/bin/bash
echo "==> Importing item_data.json into MongoDB…"
mongoimport --db itemsDB --collection itemBlock --file /data/item_data.json --jsonArray
