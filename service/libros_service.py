
import repositories.libros_repository as repository


def obtener_libros():
    lista_libros = repository.obtener_libros_r()
    if not lista_libros:
        return None
    return lista_libros 

def cargar_libro(libro : dict):
    nuevo_libro = repository.cargar_libro_r(libro)
    if not libro:
        return None
    return nuevo_libro

def aumentar_id():
    libros = repository.obtener_libros_r()
    if not libros:
        return 1
        
    return max(l['id'] for l in libros) +1



def act_libro(id, datos ):
    libro = repository.buscar_libro(id)

    if not libro:
        return None
    
    actualizaciones = datos.model_dump(exclude_unset = True )

    libro.update(actualizaciones)
    return libro

def borrar_libro(id):
    libro_eliminado = repository.eliminar_libro(id)

    if not libro_eliminado:
        return None
    
    return libro_eliminado

def filtrado_por_categoria(cat : str, lista_libros):
    return [l for l in lista_libros if l.get("categoria" , "").lower() == cat.lower()]


def filtrar_por_stock(opcion: bool , lista_libros):
    if opcion is True:
        return [l for l in lista_libros if l.get("stock",0) > 0]
    else:
        return [l for l in lista_libros if l.get("stock",0) == 0]