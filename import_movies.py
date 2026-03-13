import json
from mongo_db import connect_mongo

collection = connect_mongo()

with open("movies.json", encoding="utf-8") as f:

    for line in f:
        movie = json.loads(line)
        collection.insert_one(movie)

print("Films importés dans MongoDB")