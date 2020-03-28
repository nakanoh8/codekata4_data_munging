import csv
from pprint import pprint
# import pprint

with open('./j1.csv') as f:
    # データ読み込み
    reader = csv.reader(f)
    rows = []
    for i, row in enumerate(reader):
        if i == 0:
            continue
        sa = abs(int(row[7]) - int(row[8]))
        rows.append(row)
    pprint(sorted(rows))
    pprint(rows)

