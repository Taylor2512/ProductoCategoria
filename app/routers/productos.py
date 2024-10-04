from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.Dtos.schemas import ProductoSchemaDto
from app.models.Request.schemas import ProductoSchemaRequest
from app.dependencies.database import get_db
from typing import List
from app.crud import CRUDService

router = APIRouter(
    prefix="/productos",
    tags=["productos"]
)

def get_crud_service(db: Session = Depends(get_db)) -> CRUDService:
    return CRUDService(db)

@router.get("/", response_model=List[ProductoSchemaDto])
def read_productos(crud_service: CRUDService = Depends(get_crud_service)):
    productos = crud_service.get_productos()
    return productos

@router.get("/{id}", response_model=ProductoSchemaDto)
def get_producto_by_id(id: int,crud_service: CRUDService = Depends(get_crud_service)):
    if id == 0:
        return None
    producto = crud_service.get_producto_by_id(id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto not found")
    return producto

@router.post("/", response_model=ProductoSchemaDto)
def create_new_producto(producto: ProductoSchemaRequest, crud_service: CRUDService = Depends(get_crud_service)):
    return crud_service.create_producto(producto)