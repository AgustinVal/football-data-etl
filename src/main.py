

from extract.extract_data import extract_competitions_and_teams
from load.load_data import load_data
from export.export_csv import export_csv

#print("Pipeline iniciado correctamente. Parte Zero completada.")


if __name__ == "__main__":
    
    print("Ejecutando Parte 1 del pipeline...")
    
    data = extract_competitions_and_teams()
    
    print(f"Se extrajeron datos de {len(data)} competiciones")
    print(f"Parte Uno completada.")
    
    load_data(data)
    
    print("Parte 2 y 3.1 completada.")
    
    export_csv()
    
    print("Parte 3.2 completada.")
    
    print("Pipeline Finalizado.")
