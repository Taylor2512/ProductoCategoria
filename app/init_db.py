from sqlalchemy import create_engine, MetaData
from app.config import DATABASE_URL

def create_tables():
    engine = create_engine(DATABASE_URL)
    metadata = MetaData()
    # Aquí iría el código para definir y crear las tablas usando metadata y engine
    metadata.create_all(engine)