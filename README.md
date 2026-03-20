# Data2Excel Converter

*created: 2024/07/18*

## Overview

This tool converts input data into an Excel file.

### Project Structure

```
data2excel-converter/
├── convert.py           # Data conversion functions
├── input.py             # User input handling
├── main.py              # Main application entry point
├── output.py            # Excel output functionality
├── model/
│   ├── __init__.py
│   └── data_type_enum.py  # DataType enum definition
├── config/
│   └── config.yaml      # Configuration file
│   CHANGELOG.md         # Change logs
└── README.md            # Project documentation
```

## Supported Data Types

_*it needs to be row/column structure_

- XML
- JSON
- CSV

## Input Data Example

### XML

```xml
<root>
    <row-data>
        <name>John</name>
        <age>25</age>
    </row-data>
    <row-data>
        <name>Smith</name>
        <age>30</age>
    </row-data>
</root>
```

### JSON

```json
[
    {
        "name": "John",
        "age": 25
    },
    {
        "name": "Smith",
        "age": 30
    }
]
OR
{
    "name": {
        "1": "John",
        "2": "Smith"
    },
    "age": {
        "1": "25",
        "2": "30"  
    }
}
```

### CSV

```csv
name,age
John,25
Smith,30
```

## Dependencies

- pandas
- openpyxl
- pyyaml


## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# For development and testing
pip install -r requirements-test.txt
```

## Running Tests

This project includes a comprehensive test suite with 99% code coverage.

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=. --cov-report=html --cov-report=term

# Run specific test file
pytest tests/test_convert.py
```
