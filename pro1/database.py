from pymongo import MongoClient


def get_collections():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["students"]
    collection = db["students"]
    return collection


