import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from model.data_type_enum import DataType
import main


class TestMain:
    @patch('main.opt.print_to_excel')
    @patch('main.cvt.xml2excel')
    @patch('main.ipt.get_user_input_data')
    def test_main_xml_success(self, mock_input, mock_convert, mock_output):
        mock_input.return_value = (DataType.XML, '<root><row><name>Alice</name></row></root>')
        mock_df = pd.DataFrame({'name': ['Alice']})
        mock_convert.return_value = mock_df

        main.main()

        mock_input.assert_called_once()
        mock_convert.assert_called_once_with('<root><row><name>Alice</name></row></root>')
        mock_output.assert_called_once_with(DataType.XML, mock_df)

    @patch('main.opt.print_to_excel')
    @patch('main.cvt.json2excel')
    @patch('main.ipt.get_user_input_data')
    def test_main_json_success(self, mock_input, mock_convert, mock_output):
        mock_input.return_value = (DataType.JSON, '{"name": "Bob"}')
        mock_df = pd.DataFrame({'name': ['Bob']})
        mock_convert.return_value = mock_df

        main.main()

        mock_input.assert_called_once()
        mock_convert.assert_called_once_with('{"name": "Bob"}')
        mock_output.assert_called_once_with(DataType.JSON, mock_df)

    @patch('main.opt.print_to_excel')
    @patch('main.cvt.csv2excel')
    @patch('main.ipt.get_user_input_data')
    def test_main_csv_success(self, mock_input, mock_convert, mock_output):
        mock_input.return_value = (DataType.CSV, 'name,age\nCharlie,28')
        mock_df = pd.DataFrame({'name': ['Charlie'], 'age': [28]})
        mock_convert.return_value = mock_df

        main.main()

        mock_input.assert_called_once()
        mock_convert.assert_called_once_with('name,age\nCharlie,28')
        mock_output.assert_called_once_with(DataType.CSV, mock_df)

    @patch('builtins.print')
    @patch('main.ipt.get_user_input_data')
    def test_main_input_value_error(self, mock_input, mock_print):
        mock_input.side_effect = ValueError("Invalid data type")

        main.main()

        assert mock_print.call_count >= 2
        calls = [str(call) for call in mock_print.call_args_list]
        assert any('Input value error' in str(call) for call in calls)
        assert any('Abort the program' in str(call) for call in calls)

    @patch('builtins.print')
    @patch('main.cvt.xml2excel')
    @patch('main.ipt.get_user_input_data')
    def test_main_conversion_error(self, mock_input, mock_convert, mock_print):
        mock_input.return_value = (DataType.XML, '<invalid xml')
        mock_convert.side_effect = ValueError("XML parse error")

        main.main()

        assert mock_print.call_count >= 2
        calls = [str(call) for call in mock_print.call_args_list]
        assert any('Conversion error' in str(call) for call in calls)
        assert any('Abort the program' in str(call) for call in calls)

    @patch('builtins.print')
    @patch('main.opt.print_to_excel')
    @patch('main.cvt.json2excel')
    @patch('main.ipt.get_user_input_data')
    def test_main_handles_json_decode_error(self, mock_input, mock_convert, mock_output, mock_print):
        mock_input.return_value = (DataType.JSON, '{"invalid": json}')
        mock_convert.side_effect = ValueError("JSON parse error: Expecting value")

        main.main()

        mock_output.assert_not_called()
        assert any('Conversion error' in str(call) for call in mock_print.call_args_list)

    @patch('main.opt.print_to_excel')
    @patch('main.cvt.csv2excel')
    @patch('main.ipt.get_user_input_data')
    def test_main_convert_method_mapping(self, mock_input, mock_csv_convert, mock_output):
        # Test that the correct conversion method is called for each data type
        mock_input.return_value = (DataType.CSV, 'name\nTest')
        mock_df = pd.DataFrame({'name': ['Test']})
        mock_csv_convert.return_value = mock_df

        main.main()

        mock_csv_convert.assert_called_once()

    @patch('builtins.print')
    @patch('main.opt.print_to_excel')
    @patch('main.cvt.xml2excel')
    @patch('main.ipt.get_user_input_data')
    def test_main_does_not_print_on_success(self, mock_input, mock_convert, mock_output, mock_print):
        mock_input.return_value = (DataType.XML, '<root></root>')
        mock_convert.return_value = pd.DataFrame()

        main.main()

        # Should not print error messages
        calls = [str(call) for call in mock_print.call_args_list]
        assert not any('error' in str(call).lower() for call in calls)
        assert not any('Abort' in str(call) for call in calls)
