from ChargerDonnées.csv_loader import load_csv
from ChargerDonnées.json_loader import load_json
from ChargerDonnées.xml_loader import load_xml


def load_data_menu():
    while True:
        print("\n\n\n\n\n=== Menu de Chargement des Données ===")
        print("1. Charger depuis un fichier CSV")
        print("2. Charger depuis un fichier JSON")
        print("3. Charger depuis un fichier XML")
        print("4. Charger depuis un fichier YAML")
        print("5. Retour au menu principal")

        menu = input("Choisissez une option: ")
        if menu == "1":
            load_csv("./data/data.csv")
            print("\nCSV enregistrer ")
            break
        elif menu == "2":
            load_json("./data/data.json")
            print("\nJSON enregistrer")
            break
        elif menu == "3":
            load_xml("./data/data.xml")
            print("\nXML enregistrer")
            break
        elif menu == "4":
            print("\nYAML enregistrer")
            break
        elif menu == "5":
            print("Retour au menu principal")
            break
        else:
            print("Option invalide")
