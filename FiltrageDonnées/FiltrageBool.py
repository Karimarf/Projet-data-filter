from data_manager import DataManager


class FiltrageBool:
    dynamic_instances = DataManager.get_dynamic_instances()

    @classmethod
    def handle_filter_bool(cls, field_name):
        print("Options de filtre pour les boolean :")
        print("1. Recherche d'une valeur True")
        print("2. Recherche d'une valeur False")

        while True:
            try:
                choice = int(input("Entrez votre choix : ").strip())
                if choice == 1:
                    cls._filter_by_bool_true(field_name)
                    break
                elif choice == 2:
                    cls._filter_by_bool_false(field_name)
                    break
                else:
                    print("Veuillez entrer un numéro valide.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un numéro.")

    @classmethod
    def _filter_by_bool_true(cls, field_name):
        try:
            filtered_instances = [
                instance for instance in cls.dynamic_instances
                if True in getattr(instance, field_name)
            ]
            print(f"Résultats ({len(filtered_instances)} trouvés) :")
            for instance in filtered_instances:
                print(instance)
        except Exception as e:
            print(f"Erreur inattendue : {e}")

    @classmethod
    def _filter_by_bool_false(cls, field_name):
        try:
            filtered_instances = [
                instance for instance in cls.dynamic_instances
                if False in getattr(instance, field_name)
            ]
            print(f"Résultats ({len(filtered_instances)} trouvés) :")
            for instance in filtered_instances:
                print(instance)
        except Exception as e:
            print(f"Erreur inattendue : {e}")