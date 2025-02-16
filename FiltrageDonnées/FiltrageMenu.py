import data_manager
from FiltrageDonnées.FiltrageListe import FiltrageListe
from FiltrageDonnées.FiltrageString import FiltrageString
from FiltrageDonnées.FiltrageNumeric import FiltrageNumeric
from FiltrageDonnées.FiltrageBool import FiltrageBool


def load_filtrage_menu():
    dynamic_instances = data_manager.DataManager.get_dynamic_instances()
    if not dynamic_instances:
        print("Aucune instance à filter.")
        return

    while True:
        print("\n--------------------- MENU ---------------------")
        print("1. Afficher les données")
        print("2. Filtrer les données")
        print("3. Quitter")
        print("------------------------------------------------")
        menu = input("Veuillez choisir une option : ").strip()

        if menu == "1":
            data_manager.DataManager.get_all_instance()
        elif menu == "2":
            first_instance = dynamic_instances[0]
            columns = list(vars(first_instance).keys())
            print("Colonnes disponibles pour le filtre :")
            for index, column in enumerate(columns, start=1):
                print(f"{index}. {column}")

            try:
                choice = int(input("Entrez le numéro de la colonne pour filtrer : ")) - 1
                if 0 <= choice < len(columns):
                    field_name = columns[choice]
                    column_type = type(getattr(first_instance, field_name))

                    if column_type == str:
                        FiltrageString.handle_string_filter(field_name)
                    elif column_type in (int, float):
                        FiltrageNumeric.handle_numeric_filter(field_name)
                    elif column_type == list:
                        FiltrageListe.handle_filter_list(field_name)
                    elif column_type == bool:
                        FiltrageBool.handle_filter_bool(field_name)
                else:
                    print("Veuillez entrer un numéro valide.")
            except ValueError:
                print("Un numéro")
        elif menu == "3":
            print("Retour au menu principal.")
            break
        else:
            print("Numéro valide.")
