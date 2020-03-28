import csv
from pprint import pprint

min_temperature = 3
date = 0

def get_min_temperature(row):
    return float(row[min_temperature])

# FIXME: CSVリーダーでヘッダーを無視するようにする
with open('./weather.csv') as f:
    # データ読み込み
    reader = csv.reader(f)
    rows = []
    for i, row in enumerate(reader):
        if i == 0:
            continue
        rows.append(row)

    rows_sorted = sorted(rows, key=get_min_temperature)
    print(rows_sorted[0][date])