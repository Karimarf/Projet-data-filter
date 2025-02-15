import xml.etree.ElementTree as ET
from typing import List, Optional, Any
from data_manager import DataManager


class DataLoader:
    column_types = {}

    @classmethod
    def infer_types(cls, data: List[dict[str, str]]):
        for column in data[0].keys():
            for row in data:
                value = row[column]
                value_str = str(value)

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
                break

    @staticmethod
    def is_float(value: str) -> bool:
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_list(value: str) -> bool:
        if isinstance(value, str):
            return value.startswith("[") and value.endswith("]")
        return False

    @staticmethod
    def parse_list(value: str) -> List[Any]:
        if isinstance(value, list):
            return value

        items = value[1:-1].split(",")
        return [DataLoader.detect_type(item.strip()) for item in items]

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
                converted_value = DataLoader.convert(attr, value)
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


def load_xml(file_path: str):
    tree = ET.parse(file_path)
    root = tree.getroot()

    data = []
    headers = set()

    for element in root:
        row = {}
        for child in element:
            row[child.tag] = child.text
            headers.add(child.tag)
        data.append(row)

    headers = list(headers)
    DataLoader.infer_types(data)

    class_name = root[0].tag
    DynamicClass = ClassBuilder.create_class(class_name, headers)

    xml_instances = [
        DynamicClass(*[row.get(header, None) for header in headers]) for row in data
    ]

    DataManager.add_instances(xml_instances)

    for instance in xml_instances:
        instance.print_class()