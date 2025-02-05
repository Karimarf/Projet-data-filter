import ast
import csv

dynamic_instances = []


def create_dynamic_class(class_name, attributes):
    def __init__(self, *args):
        if len(args) != len(attributes):
            raise ValueError(f"Expected {len(attributes)} arguments, got {len(args)}")

        for attr, value in zip(attributes, args):
            # Si la valeur est une chaîne ressemblant à une liste, la convertir en liste
            if isinstance(value, str) and value.startswith("[") and value.endswith("]"):
                try:
                    value = ast.literal_eval(value)  # Convertit la chaîne en liste
                except (ValueError, SyntaxError):
                    pass  # Si la conversion échoue, laisse la valeur telle quelle
            setattr(self, attr, value)

    def __repr__(self):
        return f"{class_name}({', '.join(f'{attr}={getattr(self, attr)!r}' for attr in attributes)})"

    # Crée et retourne la classe dynamique
    return type(class_name, (object,), {"__init__": __init__, "__repr__": __repr__, "attributes": attributes})


def load_csv(file_path):
    global dynamic_instances
    with open(file_path, mode="r", newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames  # Récupère les noms des colonnes
        # Crée la classe dynamique en fonction des colonnes
        class_name = "DynamicClass"
        DynamicClass = create_dynamic_class(class_name, headers)
        # Crée les instances de la classe dynamique
        dynamic_instances = [
            DynamicClass(*[row[header] for header in headers]) for row in reader
        ]
        print(f"Données chargées et instances créées :")
        for instance in dynamic_instances:
            print(instance)
        return dynamic_instances


def get_dynamic_instances():
    return dynamic_instances
