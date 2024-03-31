import matplotlib.pyplot as plt
from matplotlib import colors
import json
import csv_to_json_parser as cjp

csv_file = r"C:\Users\USERNAME\Desktop\csv_file.csv"
json_file = r"C:\Users\USERNAME\Desktop\json_file.json"

cjp.parser(csv_file, json_file)

with open(json_file) as f:
    datadict = json.load(f)

datalist = []

for inner_dict in datadict.values():
    for key, value in inner_dict.items():
        if key == "Interacting aminoacid":
            datalist.append(value)


N, bins, patches = plt.hist(datalist, bins=len(set(datalist)))
fracs = N / N.max()
norm = colors.Normalize(fracs.min(), fracs.max())

for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

plt.title("The number of bonds that each amino acid forms")
plt.xlabel("Aminoacid")
plt.ylabel("N of bonds")

plt.show()
