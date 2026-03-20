from io import StringIO
import json
import pandas as pd
import xml.etree.ElementTree as Et


def xml2excel(xml_data):
    try:
        # Parse the XML data
        root = Et.fromstring(xml_data)

        # Extract rows and columns
        rows = []
        for row in root:
            columns = {}
            for col in row:
                columns[col.tag] = "".join(col.itertext())
            rows.append(columns)

        return pd.DataFrame(rows)

    except Et.ParseError as e:
        raise ValueError(f"XML parse error: {e}")


def json2excel(json_data):
    try:
        data = json.loads(json_data)

        return pd.DataFrame(data)

    except json.JSONDecodeError as e:
        raise ValueError(f"JSON parse error: {e}")


def csv2excel(csv_data):
    try:
        return pd.read_csv(StringIO(csv_data))
    except Exception as e:
        raise ValueError(f"CSV parse error: {e}")
