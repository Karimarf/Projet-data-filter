import csv

def load_csv(file_path):
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            for row in data:
                print(row)
            return data
