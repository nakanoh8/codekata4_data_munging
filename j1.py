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
        # sa = 0
        # if row[7] > row[8]:
        #     sa = row[7] - row[8]
        # else:
        #     sa = row[8] - row[7]
        sa = abs(int(row[7]) - int(row[8]))
        rows.append(row)
    pprint(rows)

