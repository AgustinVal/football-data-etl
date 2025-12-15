from pydantic import BaseModel

class CompetitionSummary(BaseModel):
    competition: str
    number_of_teams: int

