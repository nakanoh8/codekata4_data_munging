import csv
from pprint import pprint

def get_min_tempature(row):
    return float(row[3])

# FIXME: CSVリーダーでヘッダーを無視するようにする
with open('./wether2.csv') as f:
    # データ読み込み
    reader = csv.reader(f)
    rows = []
    for i, row in enumerate(reader):
        if i == 0:
            continue
        rows.append(row)

    rows_sorted = sorted(rows, key=get_min_tempature)
    print(rows_sorted[0][0])