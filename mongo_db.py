from pymongo import MongoClient
from config import MONGO_URI


def connect_mongo():

    client = MongoClient(MONGO_URI)

    db = client["nosql_project"]

    collection = db["movies"]

    return collection


# récupérer tous les films
def get_movies(collection):

    return list(collection.find())


# chercher un film par titre
def find_movie_by_title(collection, title):

    return collection.find_one({"title": title})


# ajouter un film
def insert_movie(collection, movie):

    collection.insert_one(movie)


# mettre à jour l'année d'un film
def update_movie_year(collection, title, new_year):

    collection.update_one(
        {"title": title},
        {"$set": {"year": new_year}}
    )


# supprimer un film
def delete_movie(collection, title):

    collection.delete_one({"title": title})