# 📚 Sistema de Gestión de Libros - API en Migración

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

Este proyecto forma parte de mi formación como desarrollador **Junior/Trainee**. Mi objetivo es construir una API robusta, evolucionando desde un almacenamiento volátil hacia una arquitectura profesional con persistencia real.

## 🎯 Objetivos y Aprendizajes
En este proceso de desarrollo estoy aplicando y consolidando los siguientes conceptos:
* **Arquitectura por Capas:** Separación de responsabilidades en `routes`, `services`, `schemas` y `db`.
* **Persistencia SQL:** Migración de datos desde listas en memoria y archivos JSON hacia **SQLite3**.
* **Validación de Datos:** Uso de **Pydantic** para garantizar la integridad de la información y el tipado fuerte.
* **Lógica de Negocio:** Implementación de filtrado, ordenamiento con funciones Lambda y "Joins" manuales entre entidades.

## 🛠️ Estado de la API (Migración Híbrida)
Actualmente, el proyecto se encuentra en una etapa de transición:

| Método | Ruta | Estado | Almacenamiento |
| :--- | :--- | :--- | :--- |
| `GET` | `/libros` | ✅ Finalizado | **SQLite** |
| `POST` | `/libros` | ✅ Finalizado | **SQLite** |
| `PUT` | `/libros/{id}` | ⚠️ Legacy | Memoria (Volátil) |
| `DELETE` | `/libros/{id}` | ⚠️ Legacy | Memoria (Volátil) |

## 📁 Estructura del Proyecto
- **`routes/`**: Controladores de las rutas y manejo de peticiones HTTP.
- **`services/`**: Lógica de negocio (procesamiento de datos y consultas SQL).
- **`schemas/`**: Modelos de Pydantic para validación de entrada y salida.
- **`db/`**: Configuración y gestión de la base de datos local.

## 🚀 Cómo ejecutar el proyecto
1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/JDileoDev/backend.git](https://github.com/JDileoDev/backend.git)
Instalar dependencias:

pip install fastapi uvicorn
Iniciar el servidor:

uvicorn main:app --reload
🚩 Próximos Desafíos
[ ] Migrar los métodos PUT y DELETE a persistencia SQL.

[ ] Implementar tabla de Categorías con relaciones (Foreign Keys).

[ ] Refactorizar el código legacy para unificar la arquitectura.

Proyecto en constante desarrollo. Enfocado en la aplicación de buenas prácticas de Backend.
