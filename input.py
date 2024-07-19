from model.data_type_enum import DataType


def get_user_input_data():
    print("Enter the type of data to convert into Excel.")

    valid_types = ', '.join([dt.value for dt in DataType])
    data_type_input = input(f"(valid types: {valid_types})\n").strip().lower()

    try:
        data_type = DataType(data_type_input)
    except ValueError:
        raise ValueError(f"Invalid data type. Please enter one of the following: {valid_types}")

    print(f"Please enter the {data_type.value.upper()} data (end with an empty line):")
    data = []
    while True:
        line = input()
        if line.strip() == "":
            break
        data.append(line)
    data = "\n".join(data)

    return data_type, data
