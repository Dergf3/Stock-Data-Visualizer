# from UserData import UserData
from StockData import StockData
# from StockChart import StockChart

# Used for testing purposes only.
# This should be moved to a separate file and used like the StockData class.
class UserData:
    def __init__(self):
        self.stock_symbol = "IBM"
        self.chart_type = 1
        self.requested_function = 2
        self.start_date = "2022-09-01"
        self.end_date = "2022-09-10"

def main():
    while True:
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
                print(f"\nStock data for {user_data.stock_symbol}:  {user_data.start_date} to {user_data.end_date}\n")
                for data in stock_data.data_dictionary.items():
                    print(data)
                # stock_chart = StockChart(user_data, stock_data)
                # stock_chart.display_chart()

            user_continue_choice = input("\nWould you like to view more stock data? Press 'y' to continue:  ")
            if user_continue_choice.lower() != "y":
                break

main()