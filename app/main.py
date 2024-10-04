from fastapi import FastAPI
from app.routers import productos, categorias
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = FastAPI()

app.include_router(productos.router)
app.include_router(categorias.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}