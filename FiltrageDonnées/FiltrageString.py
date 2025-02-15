from data_manager import DataManager


class FiltrageString:
    dynamic_instances = DataManager.get_dynamic_instances()

    @classmethod
    def handle_string_filter(cls, field_name):
        print("Options de filtre pour les chaînes :")
        print("1. Filtrer par taille (plus grand ou plus petit que la moyenne)")
        print("2. Rechercher un mot dans les chaînes")

        while True:
            choice = int(input("Entrez votre choix : "))
            if choice == 1:
                cls._filter_by_string_length(field_name)
                break
            elif choice == 2:
                cls._filter_by_word_search(field_name)
                break
            else:
                print("Veuillez entrer un numéro valide.")

    @classmethod
    def _filter_by_string_length(cls, field_name):
        lengths = [len(getattr(instance, field_name)) for instance in cls.dynamic_instances]
        average_length = sum(lengths) / len(lengths)

        print(f"La longueur moyenne des chaînes est {average_length:.2f}.")
        while True:
            comparison = input("Entrez 'plus grand' ou 'plus petit' pour filtrer : ").strip().lower()
            if comparison not in {"plus grand", "plus petit"}:
                print("Veuillez entrer 'plus grand' ou 'plus petit'.")
                continue

            if comparison == "plus grand":
                filtered_instances = [
                    instance for instance in cls.dynamic_instances
                    if len(getattr(instance, field_name)) > average_length
                ]
            else:
                filtered_instances = [
                    instance for instance in cls.dynamic_instances
                    if len(getattr(instance, field_name)) < average_length
                ]

            print(f"Résultats ({len(filtered_instances)} trouvés) :")
            for instance in filtered_instances:
                print(instance)
            break

    @classmethod
    def _filter_by_word_search(cls, field_name):
        word = input("Entrez le mot à rechercher : ").strip().lower()

        filtered_instances = [
            instance for instance in cls.dynamic_instances
            if word in getattr(instance, field_name).lower()
        ]

        print(f"Résultats ({len(filtered_instances)} trouvés) :")
        for instance in filtered_instances:
            print(instance)
