# Data2Excel Converter
*created: 2024/07/18*

## Overview
**Convert input data to excel file**

This tool converts input data into an Excel file.

## Supported Data Types
- XML
- JSON
- CSV

_*need to be row/column structure_

## Input Data Example
### XML 
```
<root>
    <row-data>
        <name>John</name>
        <age>25</age>
    </row-data>
    <row-data>
        <name>Smith</name>
        <age>30</age>
    </row-data>
</root>
```

### JSON
```
[
    {
        "name": "John",
        "age": 25
    },
    {
        "name": "Smith",
        "age": 30
    }
]
OR
{
    "name": {
        "1": "John",
        "2": "Smith"
    },
    "age": {
        "1": "25",
        "2": "30"  
    }
}
```

### CSV
```
name,age
John,25
Smith,30
```
