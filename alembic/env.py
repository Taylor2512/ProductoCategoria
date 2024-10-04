from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
import os
from alembic import context

# Importa tus modelos aquí
from app.entities.models import Base  # Ajusta la importación a tu módulo de modelos

# Este es el objeto de configuración de Alembic, que proporciona
# acceso a los valores dentro del archivo .ini en uso.
config = context.config

# Interpreta el archivo de configuración para el registro de Python.
# Esta línea básicamente configura los registradores.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Construye la URL de la base de datos a partir de las variables de entorno
db_host = os.getenv('DB_HOST', 'localhost')
db_username = os.getenv('DB_USERNAME', 'usrDobra')
db_password = os.getenv('DB_PASSWORD', 'usrD0br4')
database_url = f"mssql+pyodbc://{db_username}:{db_password}@{db_host}/pruebapy?driver=ODBC+Driver+17+for+SQL+Server"

# Configura la URL de la base de datos en la configuración
config.set_main_option('sqlalchemy.url', database_url)

# Añade el objeto MetaData de tus modelos aquí
# para soporte de 'autogenerate'
target_metadata = Base.metadata  # Asumimos que Producto y Categoria comparten el mismo MetaData

# otros valores de la configuración, definidos por las necesidades de env.py,
# pueden ser adquiridos:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def run_migrations_offline() -> None:
    """Ejecuta migraciones en modo 'offline'.

    Esto configura el contexto con solo una URL
    y no un Engine, aunque un Engine también es aceptable
    aquí. Al omitir la creación del Engine
    ni siquiera necesitamos que un DBAPI esté disponible.

    Las llamadas a context.execute() aquí emiten la cadena dada a la
    salida del script.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Ejecuta migraciones en modo 'online'.

    En este escenario necesitamos crear un Engine
    y asociar una conexión con el contexto.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()