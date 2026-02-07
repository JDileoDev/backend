from pydantic import BaseModel
from typing import List , Optional

class LibrosMostrar(BaseModel):
    id : int
    nombre : str
    categoria : str
    stock : Optional[int] = None

class LibroCargar(BaseModel):
    nombre : str
    categoria : str
    stock : Optional[int] = None

class LibroResponse(LibroCargar):
    id: int

class LibroActualizar(BaseModel):
    nombre: Optional[str] = None
    categoria: Optional[str]= None
    stock: Optional[int] = None