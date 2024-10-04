from pydantic import BaseModel
from typing import List, Optional

class CategoriaSchemaRequest(BaseModel):
    codigo: str
    nombre: str
    descripcion: str

    class Config:
        orm_mode = True

class ProductoSchemaRequest(BaseModel):
    codigo: str
    nombre: str
    img: str
    descripcion: Optional[str]
    precio: float
    id_categoria: int
    class Config:
        orm_mode = True
