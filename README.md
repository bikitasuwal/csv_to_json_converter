# CSV to JSON Converter CLI

A simple and beginner-friendly command-line tool to convert CSV files into JSON format quickly and efficiently.

---

## Features

* Convert CSV files to JSON format
* Simple and interactive command-line interface
* Uses built-in Python libraries (`csv`, `json`)
* Clean and easy-to-understand code
* Lightweight and fast

---

## Installation

```bash
pip install csvtojson-bikita==0.1.0
```

---

## Usage

Run the following command:

```bash
csvtojson-bikita
```

Then enter the required file paths:

```
Enter CSV file path:
Enter output JSON file path:
```

---

## Example Output

```json
[
    {
        "name": "John",
        "age": "25",
        "city": "New York"
    },
    {
        "name": "Alice",
        "age": "30",
        "city": "London"
    }
]
```

---

## Project Structure

```
csv-to-json-converter/
│
├── csv-to-json/
│   ├── __init__.py
│   └── converter.py
│
├── pyproject.toml
└── README.md
```

---

## Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

## License

This project is licensed under the MIT License.

---

## Author

Developed by Bikita Suwal
