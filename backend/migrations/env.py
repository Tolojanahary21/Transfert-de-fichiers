from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

from app.database.database import Base
from app.core.config import DATABASE_URL

# Import des modèles pour que Alembic détecte les tables
from app.models.device import Device
from app.models.file import File
from app.models.transfer import Transfer


# Objet Alembic Config
config = context.config


# Configuration du logging Alembic
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# Metadata utilisée par Alembic pour l'autogénération
target_metadata = Base.metadata



def run_migrations_offline() -> None:
    """
    Exécuter les migrations en mode offline
    """

    config.set_main_option(
        "sqlalchemy.url",
        DATABASE_URL
    )

    url = config.get_main_option(
        "sqlalchemy.url"
    )

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={
            "paramstyle": "named"
        },
    )

    with context.begin_transaction():
        context.run_migrations()



def run_migrations_online() -> None:
    """
    Exécuter les migrations en mode online
    """

    # Charger la connexion PostgreSQL depuis .env
    config.set_main_option(
        "sqlalchemy.url",
        DATABASE_URL
    )


    connectable = engine_from_config(
        config.get_section(
            config.config_ini_section,
            {}
        ),
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



if context.is_offline_mode():

    run_migrations_offline()

else:

    run_migrations_online()