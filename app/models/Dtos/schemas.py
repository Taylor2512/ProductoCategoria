from pydantic import BaseModel
from typing import List, Optional

class CategoriaSchemaDto(BaseModel):
    id: int
    codigo: str
    nombre: str
    descripcion: str

    class Config:
        orm_mode = True

class ProductoSchemaDto(BaseModel):
    id: int
    codigo: str
    nombre: str
    img: str
    descripcion: Optional[str]
    precio: float
    id_categoria: int
    categoria: CategoriaSchemaDto  # Relación con Categoria

    class Config:
        orm_mode = True