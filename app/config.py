import os
from dotenv import load_dotenv

load_dotenv()
# Construye la URL de la base de datos a partir de las variables de entorno
db_host = os.getenv('DB_HOST', 'localhost')
db_username = os.getenv('DB_USERNAME', 'usrDobra')
db_password = os.getenv('DB_PASSWORD', 'usrD0br4')
DATABASE_URL = f"mssql+pyodbc://{db_username}:{db_password}@{db_host}/pruebapy?driver=ODBC+Driver+17+for+SQL+Server"
