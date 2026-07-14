from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["miBaseDeDatos"]
collection = db["usuarios"]

print ("Colecciones de la base de datos:", db.list_collection_names())

print("Usuarios en la colección")
for usuario in collection.find():
    print(usuario)

# Usuario Nuevo
nuevo_usuario = {
    "nombre": "Pedro Python",
    "edad": 30,
    "intereses": ["Python", "MongoDB", "Django"]
}
resultado = collection.insert_one(nuevo_usuario)
print("Usuario insertado;", resultado.inserted_id)


#Actualizar
resultado = collection.update_one(
    {"nombre": "Pedro Python"},
    {"$set": {"edad":17}}
)
print("Documento modificado:", resultado.modified_count)