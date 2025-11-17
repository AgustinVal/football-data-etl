
import os
import json


PATH = "data"

# Guardar el diccionario como un archivo JSON dentro de /data
def save_json(data, folder, filename):
    
    path =  os.path.join(PATH, folder)
    os.makedirs(path, exist_ok=True)
    
    file_path = os.path.join(path, filename)
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
    print(f"Archivo guardado en: {file_path}")









