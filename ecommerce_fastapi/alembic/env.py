import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context


#Add your project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


#Load environment variables
from dotenv import load_dotenv
load_dotenv()

#Import your database Base and models to register metadata
from app.database import Base
from app.models.user import User
from app.models.product import Product

#Alembic Config object
config = context.config

#Setup logging from config file
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


#Override URL with value from .env
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))


#Set metadata to enable autogeneration
target_metadata = Base.metadata

def run_migrations_offline() ->None:
    """Run migrations in offline mode"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online()-> None:
    """Run migrations in online mode"""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()


#Choose mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
