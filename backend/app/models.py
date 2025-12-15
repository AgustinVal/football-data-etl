from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Competition(Base):
    __tablename__ = "dim_competitions"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Team(Base):
    __tablename__ = "dim_teams"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class FactCompetition(Base):
    __tablename__ = "fact_competitions"
    competition_id = Column(
        Integer, ForeignKey("dim_competitions.id"), primary_key=True
    )
    team_id = Column(
        Integer, ForeignKey("dim_teams.id"), primary_key=True
    )