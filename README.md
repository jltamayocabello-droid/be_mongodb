# 🍃 MongoDB - Backend Developer

![Estado del Proyecto](https://img.shields.io/badge/Estado-Completado-green)
![MongoDB Version](https://img.shields.io/badge/MongoDB-6.0%2B-47A248?logo=mongodb&logoColor=white)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Udemy Course](https://img.shields.io/badge/Curso-Backend%20Developer%20(Udemy)-ec1c24?logo=udemy&logoColor=white)

---

## 📖 Descripción del Proyecto
Este repositorio reúne el conjunto de prácticas, ejercicios y consultas desarrollados a lo largo de mi aprendizaje en el sistema de base de datos NoSQL orientado a documentos MongoDB. Todo el contenido forma parte de mi especialización académica orientada al desarrollo backend:

1. **Curso de Backend Developer (Udemy):** Un recorrido integral por el diseño, estructuración, modelado y manipulación de bases de datos NoSQL. Abarca desde la comprensión de documentos JSON/BSON, colecciones, operaciones CRUD (Create, Read, Update, Delete) básicas y avanzadas con operadores lógicos, ordenación y paginación, hasta el uso avanzado de índices, framework de agregación (pipelines), modelado de datos (documentos incrustados vs. referencias), administración del servidor (usuarios, roles, respaldos) e integración con lenguajes de programación mediante drivers (PyMongo).
2. **Prácticas en Base de Datos (`be_mongodb`):** Conjunto de scripts de consulta JS, scripts en Python (PyMongo) y respaldos en formato JSON listos para ser importados y ejecutados en una instancia local de MongoDB.

---

## 🎯 Objetivo
Consolidar el dominio técnico en el diseño, modelado, consulta y administración de bases de datos NoSQL orientadas a documentos con MongoDB bajo estándares profesionales de desarrollo backend, logrando:

- Diseñar esquemas NoSQL flexibles y eficientes adaptados a los patrones de acceso a datos (Lectura/Escritura).
- Manipular colecciones y documentos de manera ágil utilizando consultas CRUD avanzadas, proyecciones y filtros complejos.
- Optimizar el rendimiento de consultas mediante el diseño de índices simples, compuestos y el análisis de rendimiento con planes de ejecución (`explain`).
- Implementar canalizaciones de procesamiento de datos complejas mediante el Framework de Agregación de MongoDB (Aggregation Framework).
- Integrar bases de datos MongoDB con aplicaciones backend utilizando Python y el driver oficial PyMongo.

---

## 🛠️ Requerimientos Técnicos / Temas Cubiertos
Este proyecto cumple con los estándares exigidos para el aprendizaje integral del diseño y administración de bases de datos en MongoDB:

### 1. Fundamentos & Lógica NoSQL
- ✅ **Fundamentos & Documentos BSON/JSON:** Conceptos NoSQL, colecciones versus tablas, tipos de datos y organización de datos en documentos flexibles. Ejemplificado en los archivos como [miBaseDeDatos.usuarios.json](./miBaseDeDatos.usuarios.json).
- ✅ **Operaciones CRUD Básicas:** Inserción (`insertOne`, `insertMany`), consulta con filtros (`find`, `findOne`), operadores de comparación (`$gt`, `$lt`, `$eq`, etc.) y operadores de actualización/eliminación.
- ✅ **Operaciones CRUD Avanzadas:** Operadores lógicos (`$and`, `$or`, `$not`), proyección de campos, ordenamiento (`sort`) y paginación (`limit`, `skip`), junto a consultas sobre arrays (`$in`, `$all`, `$elemMatch`). Ejemplos prácticos y de prueba en [pruebas.js](./pruebas.js) y [testPyMongo.py](./testPyMongo.py).

### 2. Modelado de Datos, Agregaciones & Optimización
- ✅ **Framework de Agregación (Pipelines):** Procesamiento secuencial de documentos mediante etapas como `$match`, `$group`, `$sort` y `$project`, y operadores de acumulación (`$sum`, `$avg`, `$push`, etc.) para reportes y estadísticas (detallado en [Notas.md](./Notas.md)).
- ✅ **Modelado de Datos:** Diseño de esquemas NoSQL decidiendo de forma lógica cuándo incrustar documentos (embedding) y cuándo utilizar referencias (referencing) de acuerdo a la cardinalidad y uso de la información.
- ✅ **Optimización con Índices:** Conceptos y tipos de índices (simples, compuestos, únicos, TTL), y análisis de rendimiento usando `explain()`.

### 3. Integración, Gestión & Administración
- ✅ **Integración con Python (PyMongo):** Conexión a MongoDB local (`mongodb://localhost:27017/`), listado de colecciones, inserciones (`insert_one`) y actualizaciones (`update_one`) usando el driver oficial PyMongo, implementado en [testPyMongo.py](./testPyMongo.py).
- ✅ **Autenticación, Roles y Backups:** Respaldos y restauración de colecciones (uso de `mongoimport`), seguridad mediante roles y usuarios, y monitoreo con herramientas como MongoDB Compass.

---

## 📂 Estructura del Proyecto
```
be_mongodb/
│
├── miBaseDeDatos.usuarios.json  # Respaldo en formato JSON con la colección de usuarios de prueba
├── Notas.md                     # Apuntes teóricos de MongoDB, NoSQL, esquemas y agregaciones
├── pruebas.js                   # Consultas de prueba con operadores lógicos y filtros en MongoDB
├── README.md                    # Documentación del repositorio
├── Temario.md                   # Temario detallado y contenido estructurado del aprendizaje en MongoDB
└── testPyMongo.py               # Script de prueba e integración en Python utilizando el driver PyMongo
```

---

## 🚀 Instrucciones de Ejecución
Para ejecutar o restaurar cualquiera de los archivos de este repositorio, asegúrate de tener instalado MongoDB (Community Server o Atlas) y Python (versión 3.x recomendada) junto con el driver `pymongo` si deseas ejecutar el script de integración.

### 1. Clonar el repositorio
```bash
git clone https://github.com/jltamayocabello-droid/be_mongodb.git
cd be_mongodb
```

### 2. Importar o Restaurar Datos en MongoDB
Puedes importar el archivo de respaldo `miBaseDeDatos.usuarios.json` en una instancia de MongoDB (local) utilizando la herramienta `mongoimport` de las MongoDB Database Tools:
```bash
mongoimport --db miBaseDeDatos --collection usuarios --file miBaseDeDatos.usuarios.json --jsonArray
```
O también puedes importar el archivo JSON directamente usando la interfaz gráfica de **MongoDB Compass**.

### 3. Ejecutar el Script de Integración con Python (PyMongo)
El script `testPyMongo.py` demuestra cómo interactuar con MongoDB desde Python.

1. Instala el driver oficial `pymongo`:
   ```bash
   pip install pymongo
   ```
2. Asegúrate de que el servicio de MongoDB se esté ejecutando localmente en el puerto default `27017`.
3. Ejecuta el script:
   ```bash
   python testPyMongo.py
   ```
El script se conectará a la base de datos `miBaseDeDatos`, listará las colecciones, mostrará los usuarios existentes, insertará un nuevo usuario y finalmente lo actualizará.

---

## 📱 Áreas Técnicas Destacadas
| Área Técnica | Conceptos Clave | Descripción |
| :--- | :--- | :--- |
| 🍃 **Base de Datos NoSQL** | MongoDB, Documentos BSON | Base de datos no relacional orientada a documentos, altamente escalable y optimizada para lectura y escritura ágil de esquemas flexibles. |
| 🔍 **CRUD y Filtros Avanzados** | find, $gt, $lt, $or, $not | Consulta avanzada y manipulación de datos semiestructurados con operadores avanzados y expresiones regulares. |
| ⚡ **Framework de Agregación** | $match, $group, $sort, Pipelines | Lógica de procesamiento de datos por etapas en el servidor para generar analíticas y transformaciones robustas. |
| 📈 **Modelado e Índices** | Embedding, Referencing, Indexes | Diseño de esquemas NoSQL (incrustar vs. referenciar) y optimización de rendimiento en búsquedas mediante índices. |
| 🐍 **Integración con Python** | PyMongo, MongoClient, CRUD | Programación backend e interacción con MongoDB desde Python para manipulación automatizada de colecciones. |
| 🔒 **Administración y Backups** | mongoimport, Compass, Users | Respaldos lógicos de datos, seguridad por roles y monitoreo gráfico con Compass. |

---

## ✒️ Autor
**Jorge Tamayo Cabello**  
*Desarrollador Front-End*

---

## 📄 Licencia
Este repositorio es de carácter estrictamente académico y educativo. Todo el contenido es libre de ser consultado con fines de aprendizaje y referencia técnica.

---

## 🙏 Agradecimientos
- A **Udemy** por la excelente formación en el desarrollo de bases de datos NoSQL mediante el curso de Backend Developer.
- A la **comunidad de MongoDB** por desarrollar un motor de bases de datos NoSQL flexible, escalable y con herramientas tan intuitivas como Compass.
- A todos los desarrolladores del ecosistema de software libre que facilitan herramientas de alta calidad.
