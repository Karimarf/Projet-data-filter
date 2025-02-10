import data_manager
from ChargerDonnées.loaderMenu import load_data_menu
from Statistique.number_stat import StatsCalculator


def show_menu():
    print("\n\n\n\n\n--------------------- MENU ---------------------")
    print("1. Charger et Sauvegarder des données")
    print("2. Afficher la structure")
    print("3. Afficher les statistiques")
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
            print("Option 2:  Afficher la structure")
            data_manager.DataManager.show_columns_with_data()
            pass
        elif menu == "3":
            print("Option 4: Afficher les statistiques")
            StatsCalculator.calculate_numeric_stats()
            pass
        elif menu == "4":
            print("Option 5: Trier les données")
            pass
        elif menu == "5":
            print("Au revoir!")
            break
        else:
            print("Un nombre valide !!!!!")

