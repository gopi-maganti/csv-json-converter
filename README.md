# 🔄 CSV-JSON Converter

A simple and lightweight Python utility to convert data between **CSV** and **JSON** formats using only built-in libraries (`csv`, `json`). Perfect for learning how to work with file I/O, data transformation, and clean Python code using **type hints** and **docstrings**.

---

## 📁 Project Structure

```bash
csv-json-converter/
├── data/
│ ├── sample.csv # Input CSV file
│ └── sample.json # Output JSON file
├── src/
│ └── converter.py # Core functions for CSV ↔ JSON conversion
├── tests/
│ └── converter.py # Tests the functions for CSV ↔ JSON conversion
├── requirements.txt # Contains python packages and versions necessary to run the code
├── main.py # Main script to run conversions
└── README.md # Project documentation
```

---

## 🚀 How to Run

1. Place your CSV file in the `data/` folder (e.g., `sample.csv`).
2. Run the script:

```bash
python main.py
```

3. You’ll get:

   data/sample.json (converted from CSV)

   data/sample_converted.csv (converted back from JSON)

### 🧪 Example CSV Format

```csv
Name,Department,Location
Alice,Engineering,New York
Bob,Marketing,San Francisco
Charlie,Design,Remote
```

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

- Include unit tests using unittest or pytest

### 📜 License

This project is licensed under the MIT License.

### 🙌 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request with improvements or additional features.
