class DataManager:
    dynamic_instances = []

    @classmethod
    def add_instances(cls, instances):
        cls.dynamic_instances.extend(instances)

    @classmethod
    def get_dynamic_instances(cls):
        return cls.dynamic_instances
