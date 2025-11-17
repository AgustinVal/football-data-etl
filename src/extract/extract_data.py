
import time
from .api_client import FootballAPI
from .save_file import save_json


# Funcion para conectarse a la API y descargar la información solicitada de teams y competitions
def extract_competitions_and_teams():
    
    api = FootballAPI()
    
    print("Descargando lista de competiciones...")
    
    competitions = api.get("/competitions")["competitions"]
    
    # Guardar competiciones
    save_json(api.get("/competitions"), "competitions", "competitions.json")
    
    all_data = []
    
    for c in competitions:
        c_id = c["id"]
        c_code = c.get("code", "unknown")
        
        print(f"Descargando equipos de competición: {c_code} ({c_id})")
        
        # Se buscan resultados en los endpoints con los id's correctos para evitar error 400
        try:
            teams_json = api.get(f"/competitions/{c_id}/teams")
            teams = teams_json["teams"]
        except Exception as e:
            print(f"Error en competicion {c_id}: {e}")
            continue
        
        # Se guardanlos datos de los equipos de cada competición
        save_json(teams_json, "teams", f"{c_id}.json")
        
        all_data.append({
            "competition": c,
            "teams": teams
        })
        
        time.sleep(6) # Limite de descarga para no pasar 10 requests por minuto
    
    return all_data















