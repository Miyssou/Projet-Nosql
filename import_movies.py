import json
from mongo_db import connect_mongo

collection = connect_mongo()

count = 0

with open("movies.json", encoding="utf-8") as f:

    for line in f:

        movie = json.loads(line)

        # éviter les doublons
        if collection.find_one({"title": movie.get("title")}) is None:
            collection.insert_one(movie)
            count += 1

print(f"{count} films importés dans MongoDB")