from pprint import pprint
from common import get_rows

team_name = 1
kachiten = 7
shitten = 8

def get_rows_sorted():

def get_sa(row):
    sa = abs(int(row[kachiten]) - int(row[shitten]))
    return sa

def main():
    rows_sorted = sorted(get_rows('./j1.csv'), key=get_sa)
    print(rows_sorted[0][team_name])

main()