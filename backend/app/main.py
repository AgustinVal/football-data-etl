from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from app.db import engine
from app.schemas import CompetitionSummary

app = FastAPI()


# Configuración CORS
# Permite que el frontend (React) pueda consumir la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Frontend Vite
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    #allow_origins=["*"]
)


# EndPoint
@app.get("/summary", response_model=list[CompetitionSummary])
def get_summary():
    query = """
    SELECT c.name AS competition, COUNT(fc.team_id) AS number_of_teams
    FROM fact_competitions fc
    JOIN dim_competitions c ON fc.competition_id = c.id
    GROUP BY c.name
    ORDER BY number_of_teams DESC;
    """

    with engine.connect() as conn:
        result = conn.execute(text(query))
        return [
            {"competition": row[0], "number_of_teams": row[1]}
            for row in result
        ]