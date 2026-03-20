from datetime import datetime
import os
import pandas as pd
import yaml

from model.data_type_enum import DataType

_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_CONFIG_PATH = os.path.join(_BASE_DIR, 'config', 'config.yaml')

try:
    with open(_CONFIG_PATH) as f:
        __conf = yaml.safe_load(f)
except FileNotFoundError:
    raise FileNotFoundError(f"Config file not found: {_CONFIG_PATH}")
except yaml.YAMLError as e:
    raise ValueError(f"Config file parse error: {e}")

OUTPUT_EXCEL_DIR = __conf['output_excel_dir']


def print_to_excel(dt: DataType, df: pd.DataFrame):
    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_EXCEL_DIR):
        os.makedirs(OUTPUT_EXCEL_DIR)

    # Save the DataFrame to an Excel file
    output_file_name = dt.value + '2excel-' + str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    output_path = os.path.join(OUTPUT_EXCEL_DIR, output_file_name + '.xlsx')
    df.to_excel(output_path, index=False)

    print(f"Excel file has been created at: {output_path}")
