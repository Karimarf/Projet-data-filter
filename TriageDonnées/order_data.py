class OrderData:
    @classmethod
    def sort_by_user_choice(cls):
        if not cls.dynamic_instances:
            print("Aucune instance à trier.")
            return

        first_instance = cls.dynamic_instances[0]
        columns = list(vars(first_instance).keys())
        print("Colonnes disponibles pour le tri :")
        for index, column in enumerate(columns, start=1):
            print(f"{index}. {column}")

        while True:
            try:
                choice = int(input("Entrez le numéro de la colonne pour trier : ")) - 1
                if 0 <= choice < len(columns):
                    field_name = columns[choice]
                    break
                else:
                    print("Veuillez entrer un numéro valide.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un numéro.")

        while True:
            order = input("Entrez 'croissant' ou 'decroissant' pour l'ordre du tri : ").strip().lower()
            if order in ("croissant", "decroissant"):
                reverse = (order == "decroissant")
                break
            else:
                print("Veuillez entrer 'croissant' ou 'decroissant'.")

        try:
            cls.dynamic_instances.sort(
                key=lambda instance: cls._get_sort_value(getattr(instance, field_name)),
                reverse=reverse
            )
            print(f"Instances triées par '{field_name}'{' (décroissant)' if reverse else ''}.")
        except AttributeError:
            print(f"Erreur : Le champ '{field_name}' n'existe pas dans les instances.")

    @staticmethod
    def _get_sort_value(value):
        if isinstance(value, list):
            return sum(value) / len(value) if value else 0
        elif isinstance(value, str):
            return len(value)
        return value