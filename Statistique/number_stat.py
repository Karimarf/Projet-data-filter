from data_manager import DataManager

class StatsCalculator:
    @staticmethod
    def calculate_numeric_stats():
        numeric_stats = {}
        boolean_stats = {}
        list_stats = {}

        for instance in DataManager.get_dynamic_instances():
            for attr, value in vars(instance).items():

                if isinstance(value, (int, float)) and value not in (0,1):
                    if attr not in numeric_stats:
                        numeric_stats[attr] = []
                    numeric_stats[attr].append(value)

                elif isinstance(value, bool):
                    if attr not in boolean_stats:
                        boolean_stats[attr] = []
                    boolean_stats[attr].append(value)

                elif isinstance(value, list):
                    if attr not in list_stats:
                        list_stats[attr] = []
                    list_stats[attr].append(value)

        for attr, values in numeric_stats.items():
            min_val = min(values)
            max_val = max(values)
            avg_val = sum(values) / len(values)
            print(f"{attr} :\n  - minimum : {min_val}\n  - maximum : {max_val}\n  - moyenne : {avg_val:.2f}")

        for attr, values in boolean_stats.items():
            false_bool = sum(1 for v in values if v == False)
            true_bool = sum(1 for v in values if v == True)
            print(f"{attr} :\n  - nombre de non : {false_bool}\n  - nombre de oui : {true_bool}")

        for attr, lists in list_stats.items():
            i=1
            for values in lists:
                if all(isinstance(v, (int, float)) for v in values):
                    min_val = min(values)
                    max_val = max(values)
                    avg_val = sum(values) / len(values)
                    print(f"{attr} de la liste {i}:\n  - minimum : {min_val}\n  - maximum : {max_val}\n  - moyenne : {avg_val:.2f}")
                    i = i+1