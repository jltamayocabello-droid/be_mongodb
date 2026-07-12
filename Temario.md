# CONTENIDO

## 1. Introducción a MongoDB
    - ¿Qué es MongoDB? Conceptos básicos de una base de datos NoSQL.
    - Diferencias entre bases de datos relacionales (SQL) y no relacionales (NoSQL).
    - Carácteristicas principales: documentos, colecciones, escalabilidad horizontal.
    - Instalación de MongoDB (localmente o en la nube con MongoDB Atlas).
    - Primeros pasos: iniciar el servidor y conectarse con MongoDB Shell o Compass.

## 2. Fundamentos de datos y documentos
    - Estructura de un documento JSON7BSON
    - Colecciones v/s Tablas: como organizar datos en MongoDB
    - Tipos de datos soportados (String, Números, Arrays, Objetos aninados, etc.)
    - Crear y eliminar bases de datos
    - Crear, listar y eliminar colecciones
    
## 3. Operaciones CRUD básicas
    - Create (crear):
        - Insertar un documento ( insertOne, insertMany )
    - Read (leer):
        - Consultas básicas con find() y findOne().
        - Uso de filtros y operadores de comparación ($gt, $lt, $eq, etc)
    - Update (actualizar):
        - Modificar documentos con updateOne, updateMany .
        - Operadores de actualización ( $set, $unset, $inc, etc.)
    - Delete (eliminar):
        - Eliminar documentos con deleteOne, deleteMany .

## 4. Consultas avanzadas
    - Uso de operadores lógicos ( $and, $or, $not)
    - Proyección: limitar los campos devueltos en una consulta.
    - Ordenación ( sort ) y paginacipn ( limit, skip )
    - Consultas con arrays: $in, $all, $elemMatch .
    - Expresiones regulares para búsquedas de texto.

## 5. Índices 
    - ¿Qué son los indices y por qué son importantes?
    - Crear indices simples y compuestos.
    - Tipos de índices: únicos, TTL (time-to-live), geoespaciales.
    - Analizar rendimiento con explain() .
    - Eliminar y gestionar índices

## 6. Modelado de datos
    - Diseño de esquemas en una base de datos NoSQL.
    - Relaciones: incrustar documentos v/s referencias.
    - Operadores de agregación: $sum , $avg , $push , etc.
    - Ejemplos prácticos: estadísticas, reportes y transformaciones de datos.

## 7. Agregaciones
    - Introducción al framework de agregación.
    - Etapas comunes: $match, $group , $sort , $project .
    - Operadores de agregación: $sum , $avg , $push , etc.
    - Ejemplos prácticos: estadísticas, reportes y transformaciones de datos.
