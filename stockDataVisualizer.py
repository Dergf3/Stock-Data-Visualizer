from StockData import StockData

# Used for testing -> move to a separate file and import like StockData
class UserData:
    def __init__(self):
        self.stock_symbol = "IBM"
        self.chart_type = 1
        self.requested_function = 2
        self.start_date = "2022-09-01"
        self.end_date = "2022-09-30"

def main():
    user_data = UserData();
    stock_data = StockData(user_data.stock_symbol, user_data.requested_function)
    try:
        data_dictionary = stock_data.get_data()
    except Exception as ex:
        print(f"💥ERROR:  {ex}💥")
    else:
        for key, value in data_dictionary.items():
            print(key, value)

main()