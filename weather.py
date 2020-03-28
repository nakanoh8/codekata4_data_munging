from pprint import pprint
from common import get_rows

min_temperature = 3
date = 0

def get_min_temperature(row):
    return float(row[min_temperature])

def main():
    rows_sorted = sorted(get_rows('./weather.csv'), key=get_min_temperature)
    print(rows_sorted[0][date])

main()