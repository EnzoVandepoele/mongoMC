FROM mongo

COPY init.sh /docker-entrypoint-initdb.d/init.sh
COPY item_data.json /data/item_data.json

RUN chmod +x /docker-entrypoint-initdb.d/init.sh
