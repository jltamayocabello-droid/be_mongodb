# Carácteristicas de MongoDB - NoSQL
    - Documentos: cada registro es un documento
    Ejemplo:
    {
        "id":1,
        "nombre": "Juan",
        "edad": 24,
        "ciudad": "Madrid"
    }
    - Colección: grupo de documentos similares
    - Escalabilidad horizontal: distribuye datos en distintos servidores

# Esquemas
- ¿Que datos quiero almacenar?
- ¿Como vamos a consultar esos datos?
- ¿Que operaciones más frecuentes realizamos?

# Agregaciones
Los docs de la colección -> Pipeline -> cada etapa procesa los documentos -> nos da resultado final