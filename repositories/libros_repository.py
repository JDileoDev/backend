from database import obtener_conexion
categorias = [
    {"id": 1, "nombre": "programacion"},
    {"id": 2, "nombre": "bases de datos"}
]
libros = [    {"id": 1, "nombre": "Python", "categoria_id": 1, "stock": 10},
    {"id": 2, "nombre": "SQL", "categoria_id": 2, "stock": 5}]

def obtener_libros_r():
    return libros

def cargar_libro_r(libro : dict):
    libros.append(libro)
    return libros

def buscar_libro(id):
    for l in libros:
        if l.get("id") == id:
            return l
def eliminar_libro(id):
    for l in libros:
        if l.get("id") == id:
            libros.remove(l)
            return True
    return False

def obtener_libros_con_categoria():
    resultado = []

    for libro in libros:
        categoria = next(
            (c for c in categorias if c["id"] == libro["categoria_id"]), 
            None
        )
    
        libro_completo = libro.copy()

        if categoria:
            libro_completo["categoria"] = categoria.get("nombre","")
        
        resultado.append(libro_completo)
    return resultado


def obtener_libros_db():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre, categoria_id, stock FROM libros")

    filas = cursor.fetchall()

    conexion.close()

    libros = []
    for fila in filas:
        libros.append({
            "id": fila[0],
            "nombre": fila[1],
            "categoria_id": fila[2],
            "stock": fila[3]
        })
    return libros

def guardar_libro_db(libro: dict):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO libros (nombre,categoria_id,stock)
        VALUES (?,?, ?)
        """,
        (libro.get("nombre"), libro.get("categoria_id"), libro.get("stock"))
)
    
    conexion.commit()
    libro_id = cursor.lastrowid
    conexion.close()

    libro["id"] = libro_id

    return libro