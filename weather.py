import csv
import pprint

# FIXME: CSVリーダーでヘッダーを無視するようにする
with open('./wether2.csv') as f:
    # データ読み込み
    reader = csv.reader(f)
    rows = []
    for i, row in enumerate(reader):
        if i == 0:
            continue
        rows.append(row)

    # 最低気温日を探す
    min_tempatures = []
    for row in rows:
        min_tempatures.append(float(row[3]))
    print(min_tempatures)
    print(min(min_tempatures))

    # print(rows)