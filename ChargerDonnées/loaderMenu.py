from ChargerDonnées.csv_loader import load_csv
from ChargerDonnées.json_loader import load_json


def load_data_menu():
    while True:
        print("\n=== Menu de Chargement des Données ===")
        print("1. Charger depuis un fichier CSV")
        print("2. Charger depuis un fichier JSON")
        print("3. Charger depuis un fichier XML")
        print("4. Charger depuis un fichier YAML")
        print("q. Retour au menu principal")

        menu = input("Choisissez une option: ")

        if menu == "1":
            print("Chargement depuis un fichier CSV...")
            data = load_csv("./data/data.csv")
        elif menu == "2":
            print("Chargement depuis un fichier JSON...")
            data = load_json("./data/data.json")
        elif menu == "3":
            print("Chargement depuis un fichier XML...")
            # Appeler une fonction de chargement XML
        elif menu == "4":
            print("Chargement depuis un fichier YAML...")
            # Appeler une fonction de chargement YAML
        elif menu == "5":
            print("Retour au menu principal.")
            break
        else:
            print("Option invalide, réessayez.")
