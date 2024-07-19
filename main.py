import pandas as pd

from model.data_type_enum import DataType
import convert as cvt
import input as ipt
import output as opt


def main():
    try:
        # Get user input data
        data_type, data = ipt.get_user_input_data()
    except ValueError as e:
        print(f"Input value error: {e}")
        print("Abort the program.")
        return

    convert_method = {
        DataType.XML: cvt.xml2excel,
        DataType.JSON: cvt.json2excel,
        DataType.CSV: cvt.csv2excel
    }

    # Convert input data into a DataFrame
    try:
        df: pd.DataFrame = convert_method[data_type](data)
    except ValueError as e:
        print(f"Conversion error: {e}")
        print("Abort the program.")
        return

    # Print the DataFrame to an Excel file
    opt.print_to_excel(data_type, df)


if __name__ == "__main__":
    main()
