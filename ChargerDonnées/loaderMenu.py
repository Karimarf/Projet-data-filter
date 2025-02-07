from ChargerDonnées.csv_loader import load_csv
from ChargerDonnées.json_loader import load_json


def load_data_menu():
    while True:
        print("\n\n\n\n\n=== Menu de Chargement des Données ===")
        print("1. Charger depuis un fichier CSV")
        print("2. Charger depuis un fichier JSON")
        print("3. Charger depuis un fichier XML")
        print("4. Charger depuis un fichier YAML")
        print("5. Charger toutes les données")
        print("6. Retour au menu principal")

        menu = input("Choisissez une option: ")

        if menu == "1":
            print("\nCSV :")
            data = load_csv("./data/data.csv")
        elif menu == "2":
            print("\nJSON :")
            data = load_json("./data/data.json")
        elif menu == "3":
            print("\nXML :")
        elif menu == "4":
            print("\nYAML :")
        elif menu == "5":
            print("Chargement depuis tout les fichiers")
        elif menu == "6":
            print("Retour au menu principal")
            break
        else:
            print("Option invalide")
