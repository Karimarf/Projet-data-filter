import json

def load_json(file_path):
    with open(file_path, mode="r") as file:
        data = json.load(file)
        print(f"\nDonnées chargées depuis le fichier JSON :\n")
        for entry in data:
            print(entry)
        return data