
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base


base = declarative_base()

# Crear tabla dim_teams
class Dim_teams(base):
    
    __tablename__ = "dim_teams"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

#Crear tabla dim_competitions
class Dim_competitions(base):
    __tablename__ = "dim_competitions"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    

# Crear tabla fact_competitions
class Fact_competitions(base):
    
    __tablename__ = "fact_competitions"
    
    competition_id = Column(Integer, ForeignKey("dim_competitions.id"), primary_key=True)
    team_id = Column(Integer, ForeignKey("dim_teams.id"), primary_key=True)
    


















