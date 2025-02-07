import json
from typing import List, Optional, Any
from data_manager import DataManager


class TypeHandler:
    column_types = {}

    @classmethod
    def infer_types(cls, data: List[dict[str, str]]):
        for column in data[0].keys():  # Parcourt les colonnes
            for row in data:
                value = row[column]
                value_str = str(value)  # Convertir la valeur en chaîne de caractères

                if value_str in {"0", "1"}:
                    cls.column_types[column] = bool
                elif cls.is_list(value_str):
                    cls.column_types[column] = list
                elif value_str.isdigit():
                    cls.column_types[column] = int
                elif cls.is_float(value_str):
                    cls.column_types[column] = float
                else:
                    cls.column_types[column] = str
                break  # Une fois le type déterminé, on passe à la colonne suivante

    @staticmethod
    def is_float(value: str) -> bool:
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_list(value: str) -> bool:
        """Vérifie si une chaîne est formatée comme une liste."""
        if isinstance(value, str):
            return value.startswith("[") and value.endswith("]")
        return False

    @staticmethod
    def parse_list(value: str) -> List[Any]:
        """
        Parse une chaîne formatée comme une liste en un objet liste Python.
        Les éléments de la liste sont convertis en leur type respectif.
        """
        if isinstance(value, list):  # Si la valeur est déjà une liste, on la retourne directement
            return value

        # Si ce n'est pas déjà une liste, on suppose que c'est une chaîne formatée comme une liste
        items = value[1:-1].split(",")  # Retire les crochets et sépare les éléments
        return [TypeHandler.detect_type(item.strip()) for item in items]

    @classmethod
    def detect_type(cls, value: str):
        if value in {"0", "1"}:
            return bool(int(value))
        elif value.isdigit():
            return int(value)
        elif cls.is_float(value):
            return float(value)
        else:
            return value

    @classmethod
    def convert(cls, column: str, value: str):
        if column in cls.column_types:
            target_type = cls.column_types[column]
            try:
                if target_type == bool:
                    return bool(int(value))
                elif target_type == list:
                    return cls.parse_list(value)
                else:
                    return target_type(value)
            except ValueError:
                raise ValueError(f"Impossible de convertir '{value}' en {target_type}")
        return value


class ClassBuilder:
    @classmethod
    def build_attributes(cls, attributes_name: List[str]) -> dict[Optional[str], Optional[object]]:
        return {attr: None for attr in attributes_name}

    @classmethod
    def create_class(cls, class_name: str, attributes_name: List[str]) -> object:
        def __init__(self, *args):
            for attr, value in zip(self.__class__.attributes, args):
                converted_value = TypeHandler.convert(attr, value)
                setattr(self, attr, converted_value)

        def print_class(self):
            for attr, value in vars(self).items():
                print(f"  - {attr}: {value} ({type(value).__name__})")

        def __repr__(self):
            attributes = ", ".join(f"{attr}={repr(value)}" for attr, value in vars(self).items())
            return f"{self.__class__.__name__}({attributes})"

        new_class = cls.build_attributes(attributes_name=attributes_name)
        new_class["__init__"] = __init__
        new_class["print_class"] = print_class
        new_class["__repr__"] = __repr__
        new_class["attributes"] = attributes_name

        return type(class_name, (object,), new_class)


def load_json(file_path: str):
    with open(file_path, mode="r", encoding="utf-8") as file:
        data = json.load(file)
        TypeHandler.infer_types(data)

        headers = list(data[0].keys())
        class_name = "DynamicClass"
        DynamicClass = ClassBuilder.create_class(class_name, headers)

        json_instances = [
            DynamicClass(*[entry.get(header) for header in headers]) for entry in data
        ]

        DataManager.add_instances(json_instances)

        for instance in json_instances:
            instance.print_class()
