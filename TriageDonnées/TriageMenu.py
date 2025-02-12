import data_manager
from TriageDonnées.order_data import OrderData


def load_triage_menu():
    while True:
        print("\n--------------------- MENU ---------------------")
        print("1. Afficher les données")
        print("2. Trier les données")
        print("3. Quitter")
        print("------------------------------------------------")
        menu = input("Veuillez choisir une option : ").strip()

        if menu == "1":
            data_manager.DataManager.get_all_instance()
            pass
        elif menu == "2":
            OrderData.sort_by_user_choice()
            pass
        elif menu == "3":
            print("Menu principal")
            break
        else:
            print("Un nombre valide !!!!!")
            pass