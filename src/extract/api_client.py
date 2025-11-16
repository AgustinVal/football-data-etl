
import os
import time
import requests



class FootballAPI:
    
    URL = "https://api.football-data.org/v4"
    
    def __init__(self):
        
        self.api_key = os.getenv("API_KEY")
        
        if not self.api_key:
            raise ValueError("FOOTBALL_API_KEY no existe")
        
        self.headers = {
            "X-Auth-Token": self.api_key
        }
    
    
    def get(self, endpoint):
        
        url = f"{self.URL}{endpoint}"
        
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 429:
            
            print("Se realizaron demasiadas solicitudes, esperando 1 minuto...")
            time.sleep(60)
            
            return self.get(endpoint)
        
        if not response.ok:
            raise Exception(f"Error {response.status_code} en GET {url}: {response.text}")
        
        return response.json()

















