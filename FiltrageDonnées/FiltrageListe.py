from data_manager import DataManager


class FiltrageListe:
    dynamic_instances = DataManager.get_dynamic_instances()

    @classmethod
    def handle_filter_list(cls, field_name):
        print("Options de filtre pour les listes :")
        print("1. Rechercher une valeur dans les listes")
        print("2. Filtrer par taille de liste")
        print("3. Filtrer par rapport à une moyenne")

        while True:
            choice = int(input("Entrez votre choix : ").strip())
            if choice == 1:
                cls._filter_by_list_value(field_name)
                break
            elif choice == 2:
                cls._filter_by_list_size(field_name)
                break
            elif choice == 3:
                cls._filter_by_list_mean(field_name)
                break
            else:
                print("Veuillez entrer un numéro valide.")

    @classmethod
    def _filter_by_list_value(cls, field_name):
        value = input("Entrez la valeur à rechercher dans les listes : ").strip()
        filtered_instances = [
            instance for instance in cls.dynamic_instances
            if value in getattr(instance, field_name)
        ]
        print(f"Résultats ({len(filtered_instances)} trouvés) :")
        for instance in filtered_instances:
            print(instance)

    @classmethod
    def _filter_by_list_size(cls, field_name):
        try:
            size = int(input("Entrez la taille de liste à rechercher : ").strip())
            filtered_instances = [
                instance for instance in cls.dynamic_instances
                if len(getattr(instance, field_name)) == size
            ]

            print(f"Résultats ({len(filtered_instances)} trouvés) :")
            for instance in filtered_instances:
                print(instance)
        except ValueError:
            print("Nombre valide !!!")

    @classmethod
    def _filter_by_list_mean(cls, field_name):
        try:
            comparison_value = float(input("Entrez une valeur pour comparer à la moyenne : ").strip())
            comparison = input("Entrez 'plus grand' ou 'plus petit' pour comparer les moyennes : ").strip().lower()

            if comparison not in {"plus grand", "plus petit"}:
                print("Veuillez entrer 'plus grand' ou 'plus petit'.")
                return

            filtered_instances = []
            for instance in cls.dynamic_instances:
                lst = getattr(instance, field_name)
                if lst:
                    mean_value = sum(lst) / len(lst)
                    if (comparison == "plus grand" and mean_value > comparison_value) or \
                       (comparison == "plus petit" and mean_value < comparison_value):
                        filtered_instances.append(instance)

            print(f"Résultats ({len(filtered_instances)} trouvés) :")
            for instance in filtered_instances:
                print(instance)
        except ValueError:
            print("Nombre valide !!!")
