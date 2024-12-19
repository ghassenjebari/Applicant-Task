from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os

# Get environment variables
user = os.getenv('POSTGRES_USER', 'postgres')
password = os.getenv('POSTGRES_PASSWORD', 'password')
host = os.getenv('POSTGRES_HOST', '')
database = os.getenv('POSTGRES_DB', 'template_db')
port = os.getenv('POSTGRES_PORT', 5432)

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"connect_timeout": 10},
    # Uncomment for debug info of db creation
    # echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass
