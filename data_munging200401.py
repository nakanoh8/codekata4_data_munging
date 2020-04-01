import csv

class DataMungTmpl:
    def __init__(self):
        self.rows = []
        self.rows_sorted = []
    def read_csv_to_rows(self):
        pass
    def sort_rows(self):
        pass
    def print_first_row_target_column(self):
        pass
    # Template Method
    def data_mung_answer():
        self.read_csv_to_rows()
        self.sort_rows()
        self.print_first_row_target_column()


class DataMungWeather(DataMungTmpl):
    # get_min_temperature
    def sorted_key(self, row):
        min_temperature_column = 3
        min_temperature = float(row[min_temperature_column])
        return min_temperature
    
    def read_csv_to_rows(self):
        csv_name = './weather.csv'
        with open(csv_name) as f:
            # データ読み込み
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                # FIXME: CSVリーダーでヘッダーを無視するようにする
                if i == 0:
                    continue
                self.rows.append(row)

    def sort_rows(self):
        self.rows_sorted = sorted(self.rows, key=sorted_key)

    def print_first_row_target_column(self):
        target_column = 0
        print(self.rows_sorted[0][target_column])


class DataMungJ1(DataMungTmpl):
    # get_sa
    def sorted_key(self, row):
        kachiten_column = 7
        shitten_column = 8
        sa = abs(int(row[self.kachiten_column]) - int(row[self.shitten_column]))
        return sa
    
    def read_csv_to_rows(self):
        csv_name = './j1.csv'
        with open(csv_name) as f:
            # データ読み込み
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                # FIXME: CSVリーダーでヘッダーを無視するようにする
                if i == 0:
                    continue
                self.rows.append(row)

    def sort_rows(self):
        self.rows_sorted = sorted(self.rows, key=sorted_key)

    def print_first_row_target_column(self):
        target_column = 0
        print(self.rows_sorted[0][target_column])


DataMungWeather().data_mung_answer()
DataMungJ1().data_mung_answer()