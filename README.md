<h1>CSV to JSON parser</h1>

The parse function helps to convert a csv file to json for easy visualization of the data.

<h2>How to use?</h2>

Create your `visualisation.py` script in the same folder with `csv_to_json_parser.py`. Then import function:
```python
import csv_to_json_parser as cjp

csv_file = r"csv_file.csv"
json_file = r"json_file.json"

cjp.parser(csv_file, json_file)
```

You can see an example of visualization by downloading `example.py`

<h2>License</h2>

Distributed under the MIT License. See `LICENSE` for more information.
