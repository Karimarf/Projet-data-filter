class DataManager:
    dynamic_instances = []

    @classmethod
    def add_instances(cls, instances):
        cls.dynamic_instances.extend(instances)

    @classmethod
    def get_dynamic_instances(cls):
        return cls.dynamic_instances

    @classmethod
    def show_columns_with_data(cls):
        if not cls.dynamic_instances:
            print("Aucune instance disponible.")
            return

        print("Données des instances :")
        for index, instance in enumerate(cls.dynamic_instances, start=1):
            print(f"Instance {index}:")
            for column, value in vars(instance).items():
                print(f"  {column}: {value}")
            print()
