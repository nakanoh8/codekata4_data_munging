from pprint import pprint
from common import  get_rows_sorted, print_first_row_target_column

team_name = 1
kachiten = 7
shitten = 8

def get_sa(row):
    sa = abs(int(row[kachiten]) - int(row[shitten]))
    return sa

def main():
    rows_sorted = get_rows_sorted('./j1.csv', get_sa)
    print_first_row_target_column(rows_sorted, team_name)

main()