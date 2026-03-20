# Unit Tests for Data2Excel Converter

This directory contains comprehensive unit tests for the data2excel-converter project.

## Test Structure

```
tests/
├── __init__.py
├── conftest.py              # Pytest configuration and shared fixtures
├── test_convert.py          # Tests for conversion functions (xml2excel, json2excel, csv2excel)
├── test_input.py            # Tests for user input handling
├── test_output.py           # Tests for Excel output functionality
├── test_main.py             # Integration tests for main function
└── test_data_type_enum.py   # Tests for DataType enum
```

## Installation

Install test dependencies:

```bash
pip install -r requirements-test.txt
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run tests with coverage
```bash
pytest --cov=. --cov-report=html --cov-report=term
```

### Run specific test file
```bash
pytest tests/test_convert.py
```

### Run specific test class
```bash
pytest tests/test_convert.py::TestXml2Excel
```

### Run specific test
```bash
pytest tests/test_convert.py::TestXml2Excel::test_xml2excel_valid_data
```

### Run with verbose output
```bash
pytest -v
```

### Run and show print statements
```bash
pytest -s
```

## Test Coverage

The test suite covers:

### test_convert.py
- **TestXml2Excel**
  - Valid XML data with multiple rows
  - Single row XML
  - Nested text elements
  - Empty tags
  - Invalid XML handling
  - Empty string handling

- **TestJson2Excel**
  - Valid JSON list
  - Single JSON object
  - Nested objects
  - Empty list
  - Invalid JSON handling
  - Empty string handling
  - Null values

- **TestCsv2Excel**
  - Valid CSV data
  - Quoted fields with commas
  - Empty fields
  - Single row
  - Header only
  - Invalid CSV handling
  - Empty string handling

### test_input.py
- **TestGetUserInputData**
  - XML input handling
  - JSON input handling
  - CSV input handling
  - Case-insensitive input
  - Whitespace trimming
  - Invalid type error handling
  - Multiline input
  - Empty data handling

### test_output.py
- **TestPrintToExcel**
  - File creation
  - Directory creation
  - Filename format validation
  - File content verification
  - Empty DataFrame handling
  - Print message verification
  - Multiple data type outputs

### test_main.py
- **TestMain**
  - XML conversion flow
  - JSON conversion flow
  - CSV conversion flow
  - Input validation error handling
  - Conversion error handling
  - Error message verification
  - Conversion method mapping

### test_data_type_enum.py
- **TestDataTypeEnum**
  - Enum values
  - Enum members
  - Value lookup
  - Invalid value handling
  - Case sensitivity
  - Iteration
  - Comparison
  - Names and string representation

## Code Coverage Goals

- Aim for >80% code coverage
- All public functions should have tests
- All error paths should be tested
- Edge cases should be covered

## Writing New Tests

When adding new tests:

1. Follow the existing naming convention: `test_<function_name>_<scenario>`
2. Use descriptive test names that explain what is being tested
3. Keep tests focused on a single behavior
4. Use fixtures for common test data (defined in conftest.py)
5. Mock external dependencies (file I/O, user input, etc.)
6. Test both success and failure cases

## Continuous Integration

These tests can be integrated into CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
- name: Run tests
  run: |
    pip install -r requirements-test.txt
    pytest --cov=. --cov-report=xml
```
