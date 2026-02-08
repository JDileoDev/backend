
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