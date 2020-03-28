import csv
from pprint import pprint
# import pprint

team_name = 1
kachiten = 7
shitten = 8

with open('./j1.csv') as f:
    # データ読み込み
    reader = csv.reader(f)
    rows = []
    for i, row in enumerate(reader):
        if i == 0:
            continue
        rows.append(row)

    rows_sorted = sorted(rows, key=lambda row: abs(int(row[kachiten]) - int(row[shitten])))
    print(rows_sorted[0][team_name])