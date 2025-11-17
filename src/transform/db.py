

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Se crea la conexion a la base de datos
def get_engine():
    
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    db = os.getenv("POSTGRES_DB")
    host = os.getenv("POSTGRES_HOST", "football_test") 
    
    url = f"postgresql://{user}:{password}@{host}:5432/{db}"
    
    engine = create_engine(url)
    
    return engine

# Se hace la conexion a la base de datos junto con iniciar la sesion
def get_session():
    
    engine = get_engine()
    session = sessionmaker(bind=engine)
    
    return session()






















