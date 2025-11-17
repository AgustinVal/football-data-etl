
import os
import pandas as pd
from sqlalchemy import create_engine, text


# Se exporta el resumen en /outputs
def export_csv():
    
    print("Exportando resumen de equipos ")

    # Crear el engine con .env
    engine = create_engine(f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
                        f"@{os.getenv('DB_HOST')}:{5432}/{os.getenv('POSTGRES_DB')}")
    
    query = text("""
    SELECT c.name AS competition, COUNT(fc.team_id) AS num_teams
    FROM fact_competitions AS fc
    JOIN
    dim_competitions AS c
    ON c.id = fc.competition_id
    GROUP BY c.name
    ORDER BY num_teams DESC;
    """)
    
    # Se leen los datos usando pandas
    df = pd.read_sql(str(query), engine)
    
    # Se creq la carpeta si no existe
    os.makedirs("outputs", exist_ok=True)
    
    # Se exportan los datos a la carpeta anterior
    df.to_csv("outputs/output.csv", index=False)
    
    print("Output exportado correctamente.")










