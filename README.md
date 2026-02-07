# API de Gestión de Libros - Entrenamiento Backend

Este proyecto es una **API REST** desarrollada con **FastAPI** como parte de mi proceso de formación técnica. El objetivo principal fue implementar un CRUD completo siguiendo una **arquitectura en capas**, separando las responsabilidades de rutas, lógica de negocio y persistencia de datos.

## 🚀 Características
* **CRUD Completo**: Funcionalidades para obtener, crear, actualizar y eliminar libros.
* **Validación de Datos**: Uso de **Pydantic** para asegurar la integridad de los datos de entrada y salida.
* **Arquitectura Profesional**: Separación clara de responsabilidades para facilitar el mantenimiento y la escalabilidad.
* **Manejo de Errores**: Implementación de códigos de estado HTTP (404, 200, etc.) para respuestas claras al cliente.

## 🛠️ Estructura del Proyecto
El código está organizado de la siguiente manera:

* **`main.py`**: Punto de entrada de la aplicación y configuración del router.
* **`routes/`**: Definición de endpoints y manejo de peticiones HTTP.
* **`service/`**: Capa de lógica de negocio, incluyendo reglas de aplicación y generación de IDs.
* **`schemas/`**: Modelos de datos y validaciones con Pydantic.
* **`repositories/`**: Simulación de persistencia de datos mediante almacenamiento en memoria volátil.

## 💻 Tecnologías Utilizadas
* **Python 3.x**
* **FastAPI**
* **Pydantic**
* **Uvicorn** (Servidor ASGI)

## 🔧 Próximos Pasos (Roadmap)
Este proyecto es una base sólida que planeo expandir con:
1. Implementación de una base de datos real (SQLAlchemy + SQLite/PostgreSQL).
2. Desarrollo de una interfaz web simple con **Bootstrap**.
3. Implementación de autenticación de usuarios.

---
*Desarrollado como parte del proceso de formación técnica en el ecosistema de Python.*
