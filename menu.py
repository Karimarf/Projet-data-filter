from ChargerDonnées.loaderMenu import load_data_menu

def show_menu():
    print("\n--- MENU ---")
    print("1. Charger des données")
    print("2. Sauvegarder des données")
    print("3. Afficher la structure et les statistiques")
    print("4. Filtrer les données")
    print("5. Trier les données")
    print("6. Quitter")
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
            print("Option 2: Sauvegarder des données")
            pass
        elif menu == "3":
            print("Option 3: Afficher la structure et les statistiques")
            pass
        elif menu == "4":
            print("Option 4: Filtrer les données")
            pass
        elif menu == "5":
            print("Option 5: Trier les données")
            pass
        elif menu == "6":
            print("Au revoir!")
            break
        else:
            print("Un nombre valide !!!!!")

if __name__ == "__main__":
    main_menu()
