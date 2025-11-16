
import time
from .api_client import FootballAPI


def extract_competitions_and_teams():
    
    api = FootballAPI()
    
    print("Descargando lista de competiciones...")
    
    competitions = api.get("/competitions")["competitions"]
    
    all_data = []
    
    for c in competitions:
        c_id = c["id"]
        c_code = c.get("code")
        
        print(f"Descargando equipos de competición. {c_code} ({c_id})")
        
        try:
            teams = api.get(f"/competitions/{c_id}/teams")["teams"]
        except Exception as e:
            print(f"Error en competicion {c_id}: {e}")
            continue
        
        all_data.append({
            "competition": c,
            "teams": teams
        })
        
        time.sleep(6) # Limite de descarga para no pasar 10 requests por minuto
    
    return all_data















