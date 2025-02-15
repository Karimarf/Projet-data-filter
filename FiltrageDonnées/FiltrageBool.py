from data_manager import DataManager


class FiltrageBool:
    dynamic_instances = DataManager.get_dynamic_instances()

    @classmethod
    def handle_filter_bool(cls, field_name):
        print("Options de filtre pour les boolean :")
        print("1. Recherche d'une valeur True")
        print("2. Recherche d'une valeur False")

        while True:
            choice = int(input("Entrez votre choix : ").strip())
            if choice == 1:
                cls._filter_by_bool_true(field_name)
                break
            elif choice == 2:
                cls._filter_by_bool_false(field_name)
                break
            else:
                print("Veuillez entrer un numéro valide.")

    @classmethod
    def _filter_by_bool_true(cls, field_name):
        filtered_instances = [
            instance for instance in cls.dynamic_instances
            if True in getattr(instance, field_name)
        ]
        print(f"Résultats ({len(filtered_instances)} trouvés) :")
        for instance in filtered_instances:
            print(instance)

    @classmethod
    def _filter_by_bool_false(cls, field_name):
        filtered_instances = [
            instance for instance in cls.dynamic_instances
            if False in getattr(instance, field_name)
        ]
        print(f"Résultats ({len(filtered_instances)} trouvés) :")
        for instance in filtered_instances:
            print(instance)