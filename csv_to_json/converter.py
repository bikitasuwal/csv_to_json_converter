import csv
import json

class CSVtoJSONConverter:
    # to read csv file
    def read_csv(self, csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        print("CSV file loaded successfully")
        return data

    # to write o/p in file
    def write_json(self, data, json_file):
        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)
        print("JSON file created successfully")

    # to convert csv file to json file
    def convert(self, csv_file, json_file):
        data = self.read_csv(csv_file)
        self.write_json(data, json_file)

if __name__ == "__main__":
    print("CSV to JSON Converter")
    print("------------------------")

    csv_file = input("Enter CSV file path: ").strip().strip('"')
    json_file = input("Enter output JSON file path: ").strip().strip('"')

    converter = CSVtoJSONConverter()
    converter.convert(csv_file, json_file)