from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.Dtos.schemas import CategoriaSchemaDto
from app.models.Request.schemas import CategoriaSchemaRequest
from app.dependencies.database import get_db
from typing import List
from app.crud import CRUDService

router = APIRouter(
    prefix="/categorias",
    tags=["categorias"]
)

def get_crud_service(db: Session = Depends(get_db)) -> CRUDService:
    return CRUDService(db)

@router.get("/", response_model=List[CategoriaSchemaDto])
def read_categorias(crud_service: CRUDService = Depends(get_crud_service)):
    categorias = crud_service.get_categorias()
    return categorias

@router.get("/{id}", response_model=CategoriaSchemaDto)
def get_categoria_by_id(id: int, crud_service: CRUDService = Depends(get_crud_service)):
    if id == 0:
        return None
    categoria = crud_service.get_categoria_by_id(id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return categoria

@router.post("/", response_model=CategoriaSchemaDto)
def create_new_categoria(categoria: CategoriaSchemaRequest, crud_service: CRUDService = Depends(get_crud_service)):
    return crud_service.create_categoria(categoria)