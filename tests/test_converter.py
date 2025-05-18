import json
import csv
import os
import sys
import pytest

# Add the parent directory (project root) to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import List, Dict, Any
from src.converter import convert_csv_to_json, convert_json_to_csv

# Sample data
sample_data: List[Dict[str, Any]] = [
    {
        "Customer Id": "CUST001",
        "First Name": "John",
        "Last Name": "Doe",
        "Company": "Acme Corp",
        "City": "New York",
        "Country": "USA",
        "Phone 1": "+1-555-1234",
        "Phone 2": "+1-555-5678",
        "Email": "john.doe@example.com",
        "Subscription Date": "2023-05-10",
        "Website": "https://www.acmecorp.com"
    }
]

CSV_PATH = "test_customer.csv"
JSON_PATH = "test_customer.json"

@pytest.fixture(autouse=True)
def cleanup_files():
    """Cleanup after each test."""
    yield
    for path in [CSV_PATH, JSON_PATH, "roundtrip.csv"]:
        if os.path.exists(path):
            os.remove(path)

# ---------------------- POSITIVE TEST CASES ----------------------

def test_convert_csv_to_json(tmp_path) -> None:
    """Test converting a CSV file to JSON."""
    csv_file = tmp_path / "test.csv"
    json_file = tmp_path / "test.json"

    # Create CSV file manually
    with open(csv_file, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=sample_data[0].keys())
        writer.writeheader()
        writer.writerows(sample_data)

    convert_csv_to_json(str(csv_file), str(json_file))
    assert os.path.exists(json_file)

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        assert data == sample_data

def test_convert_json_to_csv(tmp_path) -> None:
    """Test converting a JSON file to CSV."""
    json_file = tmp_path / "test.json"
    csv_file = tmp_path / "test.csv"

    # Create JSON file manually
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, indent=4)

    convert_json_to_csv(str(json_file), str(csv_file))
    assert os.path.exists(csv_file)

    with open(csv_file, 'r', encoding='utf-8') as f:
        content = f.read()
        assert "Customer Id" in content and "John" in content

# ---------------------- NEGATIVE TEST CASES ----------------------

def test_convert_csv_to_json_file_not_found() -> None:
    """Test error when CSV input file does not exist."""
    with pytest.raises(FileNotFoundError):
        convert_csv_to_json("missing.csv", JSON_PATH)

def test_convert_json_to_csv_file_not_found() -> None:
    """Test error when JSON input file does not exist."""
    with pytest.raises(FileNotFoundError):
        convert_json_to_csv("missing.json", CSV_PATH)

def test_convert_json_to_csv_with_invalid_json(tmp_path) -> None:
    """Test error when JSON input is malformed."""
    json_file = tmp_path / "invalid.json"
    csv_file = tmp_path / "output.csv"

    with open(json_file, 'w', encoding='utf-8') as f:
        f.write("INVALID JSON")

    with pytest.raises(json.JSONDecodeError):
        convert_json_to_csv(str(json_file), str(csv_file))

def test_convert_json_to_csv_with_empty_data(tmp_path) -> None:
    """Test converting an empty JSON array to CSV should not create a file."""
    json_file = tmp_path / "empty.json"
    csv_file = tmp_path / "output.csv"

    with open(json_file, 'w', encoding='utf-8') as f:
        f.write("[]")

    convert_json_to_csv(str(json_file), str(csv_file))
    assert not os.path.exists(csv_file)
