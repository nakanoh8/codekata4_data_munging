import csv
import pprint

with open('./wether2.csv') as f:
    # データ読み込み
    reader = csv.reader(f)
    rows = []
    for row in reader:
        rows.append(row)

    # 最低気温日を探す
    min_tempatures = []
    for row in rows:
        min_tempatures.append(row[3])
        # print(min_tempature)
    print(min_tempatures)
    print(min(min_tempatures))

    # print(rows)