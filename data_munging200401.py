import csv

class DataMungTmpl:
    def __init__(self):
        self.rows = []
        self.csv_name = './***.csv'
        self.target_column = 0

    def sorted_key(self, row):
        return row

    def read_csv_to_rows(self):
        with open(self.csv_name) as f:
            # データ読み込み
            reader = csv.reader(f)
            rows = []
            for i, row in enumerate(reader):
                # FIXME: CSVリーダーでヘッダーを無視するようにする
                if i == 0:
                    continue
                self.rows.append(row)

    def sorted_rows(self):
        return sorted(self.rows, key=sorted_key)

    def print_first_row_target_column(self):
        print(self.rows[0][self.target_column])
    
    # Template Method
    def answer_data_mung(self):
        read_csv_to_rows()
        sorted_rows()
        print_first_row_target_column()


class DataMungWeather(DataMungTmpl):
    def __init__(self):
        self.csv_name = './weather.csv'
        self.target_column = 0  #date
        self.min_temperature_column = 3

    def sorted_key(self, row):
        # get_min_temperature
        min_temperature = float(row[self.min_temperature_column])
        return min_temperature


class DataMungJ1(DataMungTmpl):
    def __init__(self):
        self.csv_name = './j1.csv'
        self.target_column = 1  #team_name
        self.kachiten_column = 7
        self.shitten_column = 8

    def sorted_key(self, row):
        # get_sa
        sa = abs(int(row[self.kachiten_column]) - int(row[self.shitten_column]))
        return sa


DataMungWeather().answer_data_mung()
DataMungJ1().answer_data_mung()