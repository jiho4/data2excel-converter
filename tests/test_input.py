import pytest
from unittest.mock import patch
from model.data_type_enum import DataType
from input import get_user_input_data


class TestGetUserInputData:
    @patch('builtins.input', side_effect=['xml', '<root><row><name>Alice</name></row></root>', ''])
    def test_get_user_input_data_xml(self, mock_input):
        data_type, data = get_user_input_data()

        assert data_type == DataType.XML
        assert '<root>' in data
        assert 'Alice' in data

    @patch('builtins.input', side_effect=['json', '{"name": "Alice"}', ''])
    def test_get_user_input_data_json(self, mock_input):
        data_type, data = get_user_input_data()

        assert data_type == DataType.JSON
        assert 'Alice' in data

    @patch('builtins.input', side_effect=['csv', 'name,age', 'Alice,30', ''])
    def test_get_user_input_data_csv(self, mock_input):
        data_type, data = get_user_input_data()

        assert data_type == DataType.CSV
        assert 'name,age' in data
        assert 'Alice,30' in data

    @patch('builtins.input', side_effect=['XML', '<root></root>', ''])
    def test_get_user_input_data_case_insensitive(self, mock_input):
        data_type, data = get_user_input_data()

        assert data_type == DataType.XML

    @patch('builtins.input', side_effect=['  xml  ', '<data></data>', ''])
    def test_get_user_input_data_with_whitespace(self, mock_input):
        data_type, data = get_user_input_data()

        assert data_type == DataType.XML

    @patch('builtins.input', side_effect=['invalid'])
    def test_get_user_input_data_invalid_type(self, mock_input):
        with pytest.raises(ValueError, match="Invalid data type"):
            get_user_input_data()

    @patch('builtins.input', side_effect=['xml', 'line1', 'line2', 'line3', ''])
    def test_get_user_input_data_multiline(self, mock_input):
        data_type, data = get_user_input_data()

        assert data_type == DataType.XML
        assert data == 'line1\nline2\nline3'

    @patch('builtins.input', side_effect=['json', ''])
    def test_get_user_input_data_empty_data(self, mock_input):
        data_type, data = get_user_input_data()

        assert data_type == DataType.JSON
        assert data == ''
