import pytest
from model.data_type_enum import DataType


class TestDataTypeEnum:
    def test_enum_values(self):
        assert DataType.XML.value == 'xml'
        assert DataType.JSON.value == 'json'
        assert DataType.CSV.value == 'csv'

    def test_enum_members(self):
        assert len(DataType) == 3
        assert DataType.XML in DataType
        assert DataType.JSON in DataType
        assert DataType.CSV in DataType

    def test_enum_by_value(self):
        assert DataType('xml') == DataType.XML
        assert DataType('json') == DataType.JSON
        assert DataType('csv') == DataType.CSV

    def test_enum_invalid_value(self):
        with pytest.raises(ValueError):
            DataType('invalid')

    def test_enum_case_sensitive(self):
        with pytest.raises(ValueError):
            DataType('XML')

    def test_enum_iteration(self):
        data_types = list(DataType)
        assert len(data_types) == 3
        assert DataType.XML in data_types
        assert DataType.JSON in data_types
        assert DataType.CSV in data_types

    def test_enum_comparison(self):
        assert DataType.XML == DataType.XML
        assert DataType.XML != DataType.JSON
        assert DataType.JSON != DataType.CSV

    def test_enum_names(self):
        assert DataType.XML.name == 'XML'
        assert DataType.JSON.name == 'JSON'
        assert DataType.CSV.name == 'CSV'

    def test_enum_string_representation(self):
        assert 'DataType.XML' in str(DataType.XML)
        assert 'DataType.JSON' in str(DataType.JSON)
        assert 'DataType.CSV' in str(DataType.CSV)
