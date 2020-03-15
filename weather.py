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
    min_min_tempature = min(min_tempatures)

    result_row = [row[0] for row in rows if row[3] == str(min_min_tempature)][0]
    print(result_row)