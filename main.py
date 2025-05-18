from src.converter import csv_to_json, json_to_csv

if __name__ == "__main__":

    # Convert CSV to JSON
    csv_to_json("data/customers.csv", "data/customers_converted.json")

    # Convert JSON to CSV
    json_to_csv("data/organizations.json", "data/organizations_converted.csv")