
from fastapi import Query ,HTTPException , status , APIRouter , Depends
from typing import List , Optional 
import service.libros_service as service 
import schemas.libros_schema as schema
router = APIRouter()


@router.get("/libros" , response_model=List[schema.LibroSalida])
def mostrar_libros(
        filtros : schema.LibroFiltro = Depends(),
        limite : int =  Query(10, ge=1),
        offset : int = Query(0, ge=0), 
        orden : str | None = None    ):
    

    libros = service.obtener_libros(limite, offset,orden)
    
    if filtros.categoria:
        libros = service.filtrado_por_categoria(filtros.categoria , libros)
    
    if filtros.stock is True or filtros.stock is False:
        libros = service.filtrar_por_stock(filtros.stock , libros)

    if not service.obtener_libros(limite, offset,orden):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return libros

@router.post("/libros/cargar" )
def crear_libro(libro : schema.LibroCargar ):
    nuevo_id = service.aumentar_id()
    datos_libro = {"id" : nuevo_id , **libro.model_dump()}
    libro_nuevo = service.cargar_libro(datos_libro)
    if not libro_nuevo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="No se cargó un libro")
    return libro_nuevo

@router.put("/libros/{id}")
def actualizar_producto(id: int , datos :schema.LibroActualizar):
    libro_actualizado = service.act_libro(id, datos)

    if not libro_actualizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Libro no encontrado")

    return libro_actualizado

@router.delete("/libros/{id}")
def delete_libro(id : int ):
    libro_eliminado = service.borrar_libro(id)

    if not libro_eliminado:
        raise HTTPException(status_code=404 , detail=f"Libro no encontrado, ID:{id} no se encuentra en la lista.")
    
    return libro_eliminado
