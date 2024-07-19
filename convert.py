from io import StringIO
import json
import pandas as pd
import xml.etree.ElementTree as Et


def xml2excel(xml_data):
    try:
        # Escape special characters in XML data
        xml_data = xml_data.replace("&", "&amp;")

        # Parse the XML data
        root = Et.fromstring(xml_data)

        # Extract rows and columns
        rows = []
        for row in root:
            columns = {}
            for col in row:
                columns[col.tag] = col.text
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
    return pd.read_csv(StringIO(csv_data))
