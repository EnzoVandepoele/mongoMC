- Télécharger le projet git :  
`git clone https://github.com/EnzoVandepoele/mongoMC.git`  
- Lancer Docker Desktop  
- Ouvrez un terminal PS dans le dossier `mongo-elastic-project` du projet  
- Build le conteneur Docker :  
`docker-compose up --build -d`

**Mongo** :
- Rentrer dans la base Mongo :  
`docker exec -it mongoMC mongosh`
- Rentrer dans la database :  
`use itemsDB;`
- Vous pouvez maintenant faire vos tests. Exemple :  
`db.itemBlock.find().limit(3).pretty()`

**ElasticSearch** :  
- Rentrer dans Kiban avec l'URL suivant (port à adapter si besoin) : http://localhost:5601/
- Importer le fichier *item_data_clean.ndjson* dans MachineLearning/DataVisualizer/UploadFile
- Créé l'index "items"
- Vous pouvez maintenant faire vos tests.
- Pour voir les champs de la feuille de donnée : DataView -> items
- Pour faire des requêtes (exemple de requêtes dans le rapport) : DevTools