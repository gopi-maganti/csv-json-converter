# 🔄 CSV-JSON Converter

A simple and lightweight Python utility to convert data between **CSV** and **JSON** formats using only built-in libraries (`csv`, `json`). Perfect for learning how to work with file I/O, data transformation, and clean Python code using **type hints** and **docstrings**.

---

## 📁 Project Structure

```bash
CSV-JSON-CONVERTER/
│
├── data/ # Sample input and output files
│ ├── customers.csv
│ ├── customers.json
│ └── organizations.json
│
├── src/ # Logic for conversion
│ └── converter.py
│
├── tests/ # Unit tests for conversion functions
│ ├── test_converter.py
│ └── test_utils.py
│
├── utils.py # Reusable CSV/JSON read/write helpers
├── main.py # CLI functions to trigger conversions
├── README.md
└── .gitignore
```

---

## 📦 Requirements

- Python 3.7+
- No external dependencies (uses built-in `csv`, `json`, and `typing`)

To set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 🚀 How to Use

Convert CSV to JSON

```bash
python main.py csv-to-json data/customers.csv data/customers.json
```

Convert JSON to CSV

```bash
python main.py json-to-csv data/customers.json data/customers.csv
```

Note: You can also import and call convert_csv_to_json() or convert_json_to_csv() from main.py in your own scripts.

### 🧪 Running Tests

Tests are written using pytest.
To run all tests:

```bash

pytest tests/
```

### 🔧 Core Functions

From utils.py

- read_csv(file_path: str) -> List[Dict[str, Any]]

- write_csv(data: List[Dict[str, Any]], file_path: str) -> None

- read_json(file_path: str) -> List[Dict[str, Any]]

- write_json(data: List[Dict[str, Any]], file_path: str) -> None

From main.py

- convert_csv_to_json(csv_file_path: str, json_file_path: str) -> None

- convert_json_to_csv(json_file_path: str, csv_file_path: str) -> None

### ✨ Features

- ✅ Convert CSV to JSON (csv.reader + json.dump)

- ✅ Convert JSON to CSV (json.load + csv.writer)

- ✅ Modular code with type hints and docstrings

- ✅ Minimal, dependency-free (only Python built-ins)

### 📚 Learnings & Concepts

- Type hints for readability and maintenance

- Docstrings for documentation

- CSV and JSON file parsing

- Clean project folder organization

### 💡 Possible Extensions

- Add command-line arguments for custom file paths

- Support nested JSON structures

- Add logging and error handling

### 📜 License

This project is licensed under the MIT License.

### 🙌 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request with improvements or additional features.
