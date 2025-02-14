from data_manager import DataManager


class FiltrageNumeric:
    dynamic_instances = DataManager.get_dynamic_instances()

    @classmethod
    def handle_numeric_filter(cls, field_name):
        print("Options de filtre pour les nombres :")
        print("1. Recherche d'un nombre spécifique")
        print("2. Filtrer par intervalle")

        while True:
            try:
                choice = int(input("Entrez votre choix : "))
                if choice == 1:
                    cls._filter_by_specific_value(field_name)
                    break
                elif choice == 2:
                    cls._filter_by_range(field_name)
                    break
                else:
                    print("Veuillez entrer un numéro valide.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un numéro.")

    @classmethod
    def _filter_by_specific_value(cls, field_name):
        try:
            value = float(input("Entrez le nombre à rechercher : "))
            filtered_instances = [
                instance for instance in cls.dynamic_instances
                if getattr(instance, field_name) == value
            ]
            print(f"Résultats ({len(filtered_instances)} trouvés) :")
            for instance in filtered_instances:
                print(instance)
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre valide.")

    @classmethod
    def _filter_by_range(cls, field_name):
        try:
            min_value = float(input("Entrez la valeur minimale : "))
            max_value = float(input("Entrez la valeur maximale : "))
            if min_value > max_value:
                print("[Erreur] La valeur minimale ne peut pas être supérieure à la valeur maximale.")
                return

            filtered_instances = [
                instance for instance in cls.dynamic_instances
                if min_value <= getattr(instance, field_name) <= max_value
            ]
            print(f"Résultats ({len(filtered_instances)} trouvés) :")
            for instance in filtered_instances:
                print(instance)
        except ValueError:
            print("Entrée invalide. Veuillez entrer des nombres valides.")
