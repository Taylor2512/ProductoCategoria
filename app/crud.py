from sqlalchemy.orm import Session
from app.entities.models import Producto, Categoria
from app.models.Request.schemas import ProductoSchemaRequest, CategoriaSchemaRequest
from typing import List

class CRUDService:
    def __init__(self, db: Session):
        self.db = db

    def get_productos(self) -> List[Producto]:
        return self.db.query(Producto).all()

    def create_producto(self, producto: ProductoSchemaRequest) -> Producto:
        db_producto = Producto(**producto.dict())
        self.db.add(db_producto)
        self.db.commit()
        self.db.refresh(db_producto)
        return db_producto

    def get_categorias(self) -> List[Categoria]:
        return self.db.query(Categoria).all()

    def get_categoria_by_id(self, categoria_id: int) -> Categoria:
        return self.db.query(Categoria).filter(Categoria.id == categoria_id).first()
    
    def get_producto_by_id(self, categoria_id: int) -> Producto:
      return self.db.query(Producto).filter(Producto.id == categoria_id).first()

    def create_categoria(self, categoria: CategoriaSchemaRequest) -> Categoria:
        db_categoria = Categoria(**categoria.dict())
        self.db.add(db_categoria)
        self.db.commit()
        self.db.refresh(db_categoria)
        return db_categoria