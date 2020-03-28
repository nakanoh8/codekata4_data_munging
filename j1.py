import csv
from pprint import pprint
# import pprint

team_name = 1
kachiten = 7
shitten = 8

def get_sa(row):
    sa = abs(int(row[kachiten]) - int(row[shitten]))
    return sa

def get_rows():
    with open('./j1.csv') as f:
        # データ読み込み
        reader = csv.reader(f)
        rows = []
        for i, row in enumerate(reader):
            if i == 0:
                continue
            rows.append(row)
        return rows

# with open('./j1.csv') as f:
#     # データ読み込み
#     reader = csv.reader(f)
#     rows = []
#     for i, row in enumerate(reader):
#         if i == 0:
#             continue
#         rows.append(row)

def main():
    rows_sorted = sorted(get_rows(), key=get_sa)
    print(rows_sorted[0][team_name])

main()