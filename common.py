import csv

def get_rows(csv_name):
    with open(csv_name) as f:
        # データ読み込み
        reader = csv.reader(f)
        rows = []
        for i, row in enumerate(reader):
            # FIXME: CSVリーダーでヘッダーを無視するようにする
            if i == 0:
                continue
            rows.append(row)
        return rows