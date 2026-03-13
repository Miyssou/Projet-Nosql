from pymongo import MongoClient
from config import MONGO_URI


def connect_mongo():

    client = MongoClient(MONGO_URI)

    db = client["nosql_project"]

    collection = db["users"]

    return collection


def insert_user(collection, name, age):

    user = {
        "name": name,
        "age": age
    }

    collection.insert_one(user)


def get_users(collection):

    return list(collection.find())


def update_user(collection, name, new_age):

    collection.update_one(
        {"name": name},
        {"$set": {"age": new_age}}
    )


def delete_user(collection, name):

    collection.delete_one({"name": name})