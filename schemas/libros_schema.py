from pydantic import BaseModel
from typing import List , Optional

class LibroSalida(BaseModel):
    id : int    
    nombre : str
    categoria_id : int
    stock : int

class LibroCargar(BaseModel):
    nombre : str
    categoria_id : int
    stock : Optional[int] = None

class LibroResponse(LibroCargar):
    id: int

class LibroActualizar(BaseModel):
    nombre: Optional[str] = None
    categoria: Optional[str]= None
    stock: Optional[int] = None

class LibroCategoria(BaseModel):
    id: int
    nombre: str
    stock : Optional[int] = None

class LibroFiltro(BaseModel):
    categoria : Optional[str] = None
    stock: Optional[bool] = None

class LibroListaResponse(BaseModel):
    total: int
    data : List[LibroSalida]