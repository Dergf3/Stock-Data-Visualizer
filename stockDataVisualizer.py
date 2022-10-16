# from UserData import UserData
from StockData import StockData

# Used for testing purposes only.
# This should be moved to a separate file and used like the StockData class.
class UserData:
    def __init__(self):
        self.stock_symbol = "GOOGL"
        self.chart_type = 2
        self.requested_function = 1
        self.start_date = "2022-10-01"
        self.end_date = "2022-10-06"


def main():
    print("\nStock Data Visualizer")
    print("-----------------------")
    user_data = UserData()
    try:
        stock_data = StockData(user_data.stock_symbol, user_data.requested_function, user_data.start_date, user_data.end_date)
    except Exception as ex:
        print(f"💥ERROR:  {ex}💥")
    else:
        if not stock_data.data_dictionary.items():
            print("There was no data for the time period specified.")
        else:
            for key, value in stock_data.data_dictionary.items():
                print(key, value)

main()