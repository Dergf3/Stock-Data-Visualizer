from UserData import UserData
from StockData import StockData
from StockChart import StockChart

def main():
    while True:
        print("\nStock Data Visualizer")
        print("-----------------------")
        user_data = UserData()
        print("")
        try:
            stock_data = StockData(user_data.stock_symbol, user_data.requested_function, user_data.start_date, user_data.end_date)
        except Exception as ex:
            print(f"💥ERROR:  {ex}💥")
        else:
            if not stock_data.data_dictionary.items():
                print("There was no data for the time period specified.")
            else:
                stock_chart = StockChart(user_data, stock_data)
                stock_chart.display_chart()

            user_continue_choice = input("\nWould you like to view more stock data? Press 'y' to continue:  ")
            if user_continue_choice.lower() != "y":
                print("\nThank you for using the Stock Data Visualizer!\n")
                break

main()