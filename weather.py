from pprint import pprint
from common import get_rows_sorted, print_first_row_target_column

min_temperature = 3
date = 0

def get_min_temperature(row):
    return float(row[min_temperature])

def main():
    rows_sorted = get_rows_sorted('./weather.csv', get_min_temperature)
    print_first_row_target_column(rows_sorted, date)

main()