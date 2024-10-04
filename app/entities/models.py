from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    codigo = Column(String(255), index=True)  # Especifica el tamaño del campo
    nombre = Column(String(255), index=True)  # Especifica el tamaño del campo
    descripcion = Column(String(255), index=True)  # Especifica el tamaño del campo
    productos = relationship("Producto", back_populates="categoria")

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    codigo = Column(String(255), index=True)  # Especifica el tamaño del campo
    nombre = Column(String(255), index=True)  # Especifica el tamaño del campo
    img = Column(String(255), index=True)  # Especifica el tamaño del campo
    descripcion = Column(String(255), index=True)  # Especifica el tamaño del campo
    precio = Column(Float, nullable=True)
    id_categoria = Column(Integer, ForeignKey('categorias.id'), nullable=True)
    categoria = relationship("Categoria", back_populates="productos")