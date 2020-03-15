import csv
import pprint

with open('./wether2.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        records.append(row)
    print(records)