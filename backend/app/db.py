import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_engine():
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    db = os.getenv("POSTGRES_DB")
    host = os.getenv("POSTGRES_HOST", "postgres")

    if not all([user, password, db]):
        raise RuntimeError("Missing database environment variables")

    url = f"postgresql://{user}:{password}@{host}:5432/{db}"
    return create_engine(url)

engine = get_engine()
SessionLocal = sessionmaker(bind=engine)