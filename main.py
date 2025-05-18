from src.converter import read_csv, write_json, read_json, write_csv

if __name__ == "__main__":
    # Convert CSV to JSON
    csv_data = read_csv("data/customers.csv")
    write_json(csv_data, "data/customers.json")
    print("CSV to JSON conversion complete.")

    # Convert JSON back to CSV
    json_data = read_json("data/organizations.json")
    write_csv(json_data, "data/organizations_converted.csv")
    print("JSON to CSV conversion complete.")
