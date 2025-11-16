

from extract.extract_data import extract_competitions_and_teams

#print("Pipeline iniciado correctamente. Parte Zero completada.")


if __name__ == "__main__":
    
    print("Ejecutando Parte 1 del pipeline...")
    
    data = extract_competitions_and_teams()
    
    print(f"Se extrajeron datos de {len(data)} competiciones")
    print(f"Parte Uno completada.")
