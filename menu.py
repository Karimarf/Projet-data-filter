from ChargerDonnées.csv_loader import get_dynamic_instances
from ChargerDonnées.loaderMenu import load_data_menu

def show_menu():
    print("\n--- MENU ---")
    print("1. Charger et Sauvegarder des données")
    print("2. Afficher la structure et les statistiques")
    print("3. Filtrer les données")
    print("4. Trier les données")
    print("5. Quitter")
    print("\nVeuillez choisir une option : ", end="")

def main_menu():
    while True:
        show_menu()
        menu = input()

        if menu == "1":
            print("Option 1: Charger des données")
            load_data_menu()
            pass
        elif menu == "2":
            print("Option 3: Afficher la structure et les statistiques")
            pass
        elif menu == "3":
            print("Option 4: Filtrer les données")
            pass
        elif menu == "4":
            print("Option 5: Trier les données")
            pass
        elif menu == "5":
            print("Au revoir!")
            print(get_dynamic_instances())
            break
        else:
            print("Un nombre valide !!!!!")

if __name__ == "__main__":
    main_menu()
