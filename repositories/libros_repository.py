libros = []
categoria = []

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

def filtrar_por_cat(cat : str ):
    for l in libros:
        if l.get("categoria") == cat:
            categoria.append(l)
    return categoria