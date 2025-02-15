import csv
from data_manager import DataManager


class DataLoader:
    column_types = {}

    @classmethod
    def infer_types(cls, data):
        for column in data[0].keys():
            for row in data:
                value = row[column]
                if value in {"0", "1"}:
                    cls.column_types[column] = bool
                elif cls.is_list(value):
                    cls.column_types[column] = list
                elif value.isdigit():
                    cls.column_types[column] = int
                elif cls.is_float(value):
                    cls.column_types[column] = float
                else:
                    cls.column_types[column] = str
                break

    @staticmethod
    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_list(value):
        return value.startswith("[") and value.endswith("]")

    @staticmethod
    def parse_list(value):
        items = value[1:-1].split(",")
        return [DataLoader.detect_type(item.strip()) for item in items]

    @classmethod
    def detect_type(cls, value):
        if value in {"0", "1"}:
            return bool(int(value))
        elif value.isdigit():
            return int(value)
        elif cls.is_float(value):
            return float(value)
        else:
            return value

    @classmethod
    def convert(cls, column, value):
        if column in cls.column_types:
            target_type = cls.column_types[column]

            if target_type == bool:
                return bool(int(value))
            elif target_type == list:
                return cls.parse_list(value)
            else:
                return target_type(value)
        return value


class ClassBuilder:
    @classmethod
    def build_attributes(cls, attributes_name):
        return {attr: None for attr in attributes_name}

    @classmethod
    def create_class(cls, class_name, attributes_name):
        def __init__(self, *args):
            for attr, value in zip(self.__class__.attributes, args):
                converted_value = DataLoader.convert(attr, value)
                setattr(self, attr, converted_value)

        def __repr__(self):
            attributes = ", ".join(f"{attr}={repr(value)}" for attr, value in vars(self).items())
            return f"{self.__class__.__name__}({attributes})"

        new_class = cls.build_attributes(attributes_name=attributes_name)
        new_class["__init__"] = __init__
        new_class["__repr__"] = __repr__
        new_class["attributes"] = attributes_name

        return type(class_name, (object,), new_class)


def load_csv(file_path):
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        data = list(reader)
        headers = reader.fieldnames

        DataLoader.infer_types(data)

        class_name = "DATA"
        DynamicClass = ClassBuilder.create_class(class_name, headers)

        csv_instances = [
            DynamicClass(*[row[header] for header in headers]) for row in data
        ]

        DataManager.add_instances(csv_instances)
