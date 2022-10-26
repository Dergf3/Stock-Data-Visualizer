import pygal

class Stocks:
    def __init__(self, user_data, stock_data):
        self.user_data = user_data
        self.stock_data = stock_data
        self.open_list = []
        self.high_list = []
        self.low_list = []
        self.close_list = []
        self._populate_chart_list()
        self.date_list = []

def __populate_chart_list(self):
    for key, value in self.stock_data.data_dictionary.items():
        self.date_list.append(key)
        for keyTwo, valueTwo in value.items():
            if 'open' in keyTwo:
                valueTwo_number = float(valueTwo)
                self.open_list.append(valueTwo_number)
            if 'high' in keyTwo:
                valueTwo_number = float(valueTwo)
                self.high_list.append(valueTwo_number)
            if 'low' in keyTwo:
                valueTwo_number = float(valueTwo)
                self.low_list.append(valueTwo_number)
            if 'close' in keyTwo:
                valueTwo_number = float(valueTwo)
                self.close_list.append(valueTwo_number)            
