
from transform.db import get_engine, get_session
from transform.models import base, Dim_teams, Dim_competitions, Fact_competitions



def load_data(extracted_data):
    
    # Se inicializa la conexion a la base de datos    
    engine = get_engine()
    base.metadata.create_all(engine) # Crear todas las tablas
    session = get_session()
    
    print("Intertando datos en PostgreSQL...")
    
    for e in extracted_data:
        teams = e["teams"]
        comp = e["competition"]
        
        # Se insertan datos en dim_competitions
        competition = Dim_competitions(id=comp["id"], name=comp["name"])
        session.merge(competition)
        
        # Se insertan los datos de teams y fact_competitions
        for t in teams:
            
            team = Dim_teams(id=t["id"], name=t["name"])
            session.merge(team)
            
            fact = Fact_competitions(competition_id=comp["id"], team_id=t["id"])
            session.merge(fact)
    
    session.commit()
    session.close()
    
    print("Datos cargados.")



























