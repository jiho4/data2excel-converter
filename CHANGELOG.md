# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0-SNAPSHOT] - 2026-03-19

### Added

- Comprehensive unit test suite with pytest
  - 52 tests covering all modules with 99% code coverage
  - Tests for XML, JSON, and CSV conversion functions
  - Tests for user input handling
  - Tests for Excel output functionality
  - Integration tests for main application flow
  - Tests for DataType enum
- Test infrastructure files:
  - `pytest.ini` - Pytest configuration
  - `requirements-test.txt` - Test dependencies
  - `tests/conftest.py` - Shared test fixtures
  - `tests/README.md` - Test documentation
  - `TEST_SUMMARY.md` - Comprehensive test summary
- Version tracking with `__version__.py`
- This CHANGELOG.md file

### Changed

- Refactored overall code

### Fixed

- **convert.py**:
  - Removed incorrect `&` character escaping in `xml2excel` that caused double-escaping
  - Fixed nested element text extraction using `itertext()` instead of `text`
  - Added error handling to `csv2excel` for consistent error reporting
- **output.py**:
  - Changed config file path to use `__file__`-based absolute path for better portability
  - Added error handling for config file loading (`FileNotFoundError` and `yaml.YAMLError`)
- **main.py**:
  - Removed unused `import pandas as pd`

## [1.0.0] - 2024-07-19

### Added

- Initial project creation
- Core functionality to convert data formats to Excel:
  - XML to Excel conversion
  - JSON to Excel conversion
  - CSV to Excel conversion
- User input interface for data type selection
- Excel file output with timestamped filenames
- Configuration file support (YAML)
- DataType enum for type safety
