import pytest
import pandas as pd
import os
import tempfile
import shutil
from unittest.mock import patch, MagicMock
from model.data_type_enum import DataType
import output


class TestPrintToExcel:
    @pytest.fixture
    def temp_output_dir(self):
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)

    @pytest.fixture
    def sample_dataframe(self):
        return pd.DataFrame({
            'name': ['Alice', 'Bob'],
            'age': [30, 25],
            'city': ['NYC', 'LA']
        })

    @patch('output.OUTPUT_EXCEL_DIR')
    def test_print_to_excel_creates_file(self, mock_dir, temp_output_dir, sample_dataframe):
        mock_dir.__str__ = lambda self: temp_output_dir
        output.OUTPUT_EXCEL_DIR = temp_output_dir

        output.print_to_excel(DataType.XML, sample_dataframe)

        files = os.listdir(temp_output_dir)
        assert len(files) == 1
        assert files[0].startswith('xml2excel-')
        assert files[0].endswith('.xlsx')

    @patch('output.OUTPUT_EXCEL_DIR')
    def test_print_to_excel_creates_directory(self, mock_dir, sample_dataframe):
        temp_dir = tempfile.mkdtemp()
        non_existent_dir = os.path.join(temp_dir, 'output')

        try:
            output.OUTPUT_EXCEL_DIR = non_existent_dir

            output.print_to_excel(DataType.JSON, sample_dataframe)

            assert os.path.exists(non_existent_dir)
            files = os.listdir(non_existent_dir)
            assert len(files) == 1
            assert files[0].startswith('json2excel-')
        finally:
            shutil.rmtree(temp_dir)

    @patch('output.OUTPUT_EXCEL_DIR')
    def test_print_to_excel_correct_filename_format(self, mock_dir, temp_output_dir, sample_dataframe):
        output.OUTPUT_EXCEL_DIR = temp_output_dir

        output.print_to_excel(DataType.CSV, sample_dataframe)

        files = os.listdir(temp_output_dir)
        filename = files[0]

        assert filename.startswith('csv2excel-')
        assert '.xlsx' in filename
        # Check timestamp format (YYYY-MM-DD-HH-MM-SS)
        timestamp_part = filename.replace('csv2excel-', '').replace('.xlsx', '')
        parts = timestamp_part.split('-')
        assert len(parts) == 6  # year, month, day, hour, minute, second

    @patch('output.OUTPUT_EXCEL_DIR')
    def test_print_to_excel_file_content(self, mock_dir, temp_output_dir, sample_dataframe):
        output.OUTPUT_EXCEL_DIR = temp_output_dir

        output.print_to_excel(DataType.XML, sample_dataframe)

        files = os.listdir(temp_output_dir)
        output_file = os.path.join(temp_output_dir, files[0])

        # Read the Excel file back
        df_read = pd.read_excel(output_file)

        assert len(df_read) == 2
        assert list(df_read.columns) == ['name', 'age', 'city']
        assert df_read.iloc[0]['name'] == 'Alice'
        assert df_read.iloc[1]['age'] == 25

    @patch('output.OUTPUT_EXCEL_DIR')
    def test_print_to_excel_empty_dataframe(self, mock_dir, temp_output_dir):
        output.OUTPUT_EXCEL_DIR = temp_output_dir
        empty_df = pd.DataFrame()

        output.print_to_excel(DataType.JSON, empty_df)

        files = os.listdir(temp_output_dir)
        assert len(files) == 1

    @patch('output.OUTPUT_EXCEL_DIR')
    @patch('builtins.print')
    def test_print_to_excel_prints_message(self, mock_print, mock_dir, temp_output_dir, sample_dataframe):
        output.OUTPUT_EXCEL_DIR = temp_output_dir

        output.print_to_excel(DataType.XML, sample_dataframe)

        mock_print.assert_called_once()
        call_args = mock_print.call_args[0][0]
        assert 'Excel file has been created at:' in call_args
        assert 'xml2excel-' in call_args

    @patch('output.OUTPUT_EXCEL_DIR')
    def test_print_to_excel_multiple_datatypes(self, mock_dir, temp_output_dir, sample_dataframe):
        output.OUTPUT_EXCEL_DIR = temp_output_dir

        output.print_to_excel(DataType.XML, sample_dataframe)
        output.print_to_excel(DataType.JSON, sample_dataframe)
        output.print_to_excel(DataType.CSV, sample_dataframe)

        files = os.listdir(temp_output_dir)
        assert len(files) == 3
        assert any('xml2excel-' in f for f in files)
        assert any('json2excel-' in f for f in files)
        assert any('csv2excel-' in f for f in files)
