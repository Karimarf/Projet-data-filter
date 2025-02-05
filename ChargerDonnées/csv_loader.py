import csv
from typing import List, Optional

dynamic_instances = []


class ClassBuilder:
    @classmethod
    def build_attributes(cls, attributes_name: List[str]) -> dict[Optional[str], Optional[object]]:
        return {attr: None for attr in attributes_name}

    @classmethod
    def create_class(cls, class_name: str, attributes_name: List[str]) -> object:

        def __init__(self, *args):
            if len(args) != len(self.__class__.attributes):
                raise ValueError(
                    f"Expected {len(self.__class__.attributes)} arguments, got {len(args)}"
                )
            for attr, value in zip(self.__class__.attributes, args):
                setattr(self, attr, value)

        def print_class(self):
            print(f"Class Name: {self.__class__.__name__}")
            print("Attributes:")
            for attr, value in vars(self).items():
                print(f"  - {attr}: {value}")

        new_class = cls.build_attributes(attributes_name=attributes_name)

        new_class["__init__"] = __init__
        new_class["print_class"] = print_class
        new_class["attributes"] = attributes_name

        return type(class_name, (object,), new_class)


def load_csv(file_path: str):
    global dynamic_instances
    with open(file_path, mode="r", newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames

        class_name = "DynamicClass"
        DynamicClass = ClassBuilder.create_class(class_name, headers)

        dynamic_instances = [
            DynamicClass(*[row[header] for header in headers]) for row in reader
        ]

        print(f"Données CSV chargées et instances créées :")
        for instance in dynamic_instances:
            instance.print_class()

        return dynamic_instances


def get_dynamic_instances():
    return dynamic_instances
