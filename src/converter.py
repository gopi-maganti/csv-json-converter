"""
Python script to convert CSV files to JSON and vice versa.
"""

import csv
import json
from typing import List, Dict, Any

def read_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Reads a CSV file and returns a list of dictionaries.
    Each dictionary represents a row in the CSV file.
    """
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def write_json(data: List[Dict[str, Any]], file_path: str) -> None:
    """
    Writes a list of dictionaries to a JSON file.
    Each dictionary represents a row in the CSV file.
    """
    with open(file_path, mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def read_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Reads a JSON file and returns a list of dictionaries.
    Each dictionary represents a row in the CSV file.
    """
    with open(file_path, mode='r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def write_csv(data: List[Dict[str, Any]], file_path: str) -> None:
    """
    Writes a list of dictionaries to a CSV file.
    Each dictionary represents a row in the CSV file.
    """
    if not data:
        return
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
