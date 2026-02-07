
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
    id = 1
    lista_libros = repository.obtener_libros_r()
    for l in lista_libros:
        if l.get("id") == id :
            id +=1
    return id



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