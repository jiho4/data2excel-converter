import pytest
import pandas as pd
from convert import xml2excel, json2excel, csv2excel


class TestXml2Excel:
    def test_xml2excel_valid_data(self):
        xml_data = """
        <root>
            <row>
                <name>Alice</name>
                <age>30</age>
                <city>New York</city>
            </row>
            <row>
                <name>Bob</name>
                <age>25</age>
                <city>Los Angeles</city>
            </row>
        </root>
        """
        df = xml2excel(xml_data)

        assert isinstance(df, pd.DataFrame)
        assert len(df) == 2
        assert list(df.columns) == ['name', 'age', 'city']
        assert df.iloc[0]['name'] == 'Alice'
        assert df.iloc[1]['name'] == 'Bob'

    def test_xml2excel_single_row(self):
        xml_data = """
        <root>
            <row>
                <id>1</id>
                <value>test</value>
            </row>
        </root>
        """
        df = xml2excel(xml_data)

        assert len(df) == 1
        assert df.iloc[0]['id'] == '1'
        assert df.iloc[0]['value'] == 'test'

    def test_xml2excel_nested_text(self):
        xml_data = """
        <root>
            <row>
                <name>John <middle>Middle</middle> Doe</name>
            </row>
        </root>
        """
        df = xml2excel(xml_data)

        assert 'Middle' in df.iloc[0]['name']

    def test_xml2excel_empty_tags(self):
        xml_data = """
        <root>
            <row>
                <name>Alice</name>
                <age></age>
            </row>
        </root>
        """
        df = xml2excel(xml_data)

        assert df.iloc[0]['age'] == ''

    def test_xml2excel_invalid_xml(self):
        xml_data = "<root><row><name>Alice</row>"

        with pytest.raises(ValueError, match="XML parse error"):
            xml2excel(xml_data)

    def test_xml2excel_empty_string(self):
        with pytest.raises(ValueError, match="XML parse error"):
            xml2excel("")


class TestJson2Excel:
    def test_json2excel_valid_list(self):
        json_data = '[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]'
        df = json2excel(json_data)

        assert isinstance(df, pd.DataFrame)
        assert len(df) == 2
        assert df.iloc[0]['name'] == 'Alice'
        assert df.iloc[1]['age'] == 25

    def test_json2excel_single_object(self):
        # Single objects without a list wrapper require pandas to have an index
        # Wrapping in a list is the standard approach for single records
        json_data = '[{"name": "Alice", "age": 30}]'
        df = json2excel(json_data)

        assert isinstance(df, pd.DataFrame)
        assert len(df) == 1
        assert df.iloc[0]['name'] == 'Alice'
        assert df.iloc[0]['age'] == 30

    def test_json2excel_nested_objects(self):
        json_data = '[{"name": "Alice", "address": {"city": "NYC"}}]'
        df = json2excel(json_data)

        assert isinstance(df, pd.DataFrame)
        assert 'name' in df.columns
        assert 'address' in df.columns

    def test_json2excel_empty_list(self):
        json_data = '[]'
        df = json2excel(json_data)

        assert isinstance(df, pd.DataFrame)
        assert len(df) == 0

    def test_json2excel_invalid_json(self):
        json_data = '{"name": "Alice", "age": 30'

        with pytest.raises(ValueError, match="JSON parse error"):
            json2excel(json_data)

    def test_json2excel_empty_string(self):
        with pytest.raises(ValueError, match="JSON parse error"):
            json2excel("")

    def test_json2excel_with_null_values(self):
        json_data = '[{"name": "Alice", "age": null}]'
        df = json2excel(json_data)

        assert pd.isna(df.iloc[0]['age'])


class TestCsv2Excel:
    def test_csv2excel_valid_data(self):
        csv_data = "name,age,city\nAlice,30,NYC\nBob,25,LA"
        df = csv2excel(csv_data)

        assert isinstance(df, pd.DataFrame)
        assert len(df) == 2
        assert list(df.columns) == ['name', 'age', 'city']
        assert df.iloc[0]['name'] == 'Alice'
        assert df.iloc[1]['city'] == 'LA'

    def test_csv2excel_with_quotes(self):
        csv_data = 'name,description\n"Alice","A person, who lives in NYC"'
        df = csv2excel(csv_data)

        assert df.iloc[0]['description'] == 'A person, who lives in NYC'

    def test_csv2excel_empty_fields(self):
        csv_data = "name,age,city\nAlice,,NYC"
        df = csv2excel(csv_data)

        assert pd.isna(df.iloc[0]['age'])

    def test_csv2excel_single_row(self):
        csv_data = "name,age\nAlice,30"
        df = csv2excel(csv_data)

        assert len(df) == 1

    def test_csv2excel_header_only(self):
        csv_data = "name,age,city"
        df = csv2excel(csv_data)

        assert len(df) == 0
        assert list(df.columns) == ['name', 'age', 'city']

    def test_csv2excel_invalid_csv(self):
        # Pandas read_csv is lenient and handles extra columns by default
        # Test with truly malformed CSV that would cause an error
        csv_data = 'name,age\n"Alice,30'  # Unclosed quote

        with pytest.raises(ValueError, match="CSV parse error"):
            csv2excel(csv_data)

    def test_csv2excel_empty_string(self):
        with pytest.raises(ValueError, match="CSV parse error"):
            csv2excel("")
