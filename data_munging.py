import csv

class DataMungTmpl:
    def __init__(self):
        self.csv_name = './***.csv'
        self.target_column = 0

    def sorted_key(self, row):
        return row

    def get_rows(self):
        with open(self.csv_name) as f:
            # データ読み込み
            reader = csv.reader(f)
            rows = []
            for i, row in enumerate(reader):
                # FIXME: CSVリーダーでヘッダーを無視するようにする
                if i == 0:
                    continue
                rows.append(row)
            return rows

    def get_rows_sorted(self, rows):
        return sorted(rows, key=self.sorted_key)

    def get_first_row_target_column(self, rows_sorted):
        return rows_sorted[0][self.target_column]
    
    def print_answer(self):
        print(self.get_first_row_target_column(self.get_rows_sorted(self.get_rows())))


class DataMungWeather(DataMungTmpl):
    def __init__(self):
        self.csv_name = './weather.csv'
        self.target_column = 0  #date
        self.min_temperature_column = 3

    # get_min_temperature
    def sorted_key(self, row):
        min_temperature = float(row[self.min_temperature_column])
        return min_temperature


class DataMungJ1(DataMungTmpl):
    def __init__(self):
        self.csv_name = './j1.csv'
        self.target_column = 1  #team_name
        self.kachiten_column = 7
        self.shitten_column = 8

    # get_sa
    def sorted_key(self, row):
        sa = abs(int(row[self.kachiten_column]) - int(row[self.shitten_column]))
        return sa


DataMungWeather().print_answer()
DataMungJ1().print_answer()