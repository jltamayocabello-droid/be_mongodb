from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["miBaseDeDatos"]
collection = db["usuarios"]

print ("Colecciones de la base de datos:", db.list_collection_names())