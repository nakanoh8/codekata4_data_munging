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

def get_rows_sorted(csv_name, key):
    return sorted(get_rows(csv_name), key=key)

def print_first_row_target_column(rows_sorted, target_column):
    print(rows_sorted[0][target_column])