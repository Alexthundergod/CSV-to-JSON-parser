import csv
import json
import re


def parser(csv_file, json_file):
    datadict = {}

    with open(csv_file) as csvf:
        spamreader = csv.reader(csvf, dialect="excel", quotechar="|")
        datalist = [
            str(row)
            .replace("['", "")
            .replace("п»ї", "")
            .replace("']", "")
            .replace("', '", ", ")
            .split(";")
            for row in spamreader
        ]
        datalist = [
            [re.sub(r"(\d), (\d)", r"\1.\2", i) for i in datalist[j]]
            for j in range(0, len(datalist))
        ]
        header = [i for i in datalist[0]]

        for row in datalist[1:]:
            tempdict = {}
            for item in row:
                try:
                    tempdict[f"{header[row.index(item)]}"] = float(item)
                except ValueError:
                    tempdict[f"{header[row.index(item)]}"] = item

            datadict[int(f"{datalist.index(row)-1}")] = tempdict

        print(datadict)

    with open(json_file, "w") as f:
        json.dump(datadict, f)
