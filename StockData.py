import requests

# Assumption of the user object
# class UserData:
#     def __init__(self):
#         self.stock_symbol = "IBM"
#         self.chart_type = 1
#         self.requested_function = 2
#         self.start_date = "2022-09-01"
#         self.end_date = "2022-09-30"

"""
    Use: stock_data = StockData(user_data.stock_symbol, user_data.requested_function)
         stock_data_dictionary = stock_data.get_data()
"""
class StockData:
    def __init__(self, stock_symbol: str, requested_function: int):
        self.__API_KEY = "EYRT2L2R3HI4L78O"
        self.__stock_symbol = stock_symbol
        self.__interval = "5min" # Do we allow the user to set this? This wasn't in the video or requirements. Allowed values are: 1min, 5min, 15min, 30min, 60min

        # Set requested function with respective string value
        if requested_function == 1:
            self.__requested_function = "INTRADAY" # Returns only the last 100 data points unless we add another url parameter
            self.__key_name = f"Time Series ({self.__interval})"
        elif requested_function == 2:
            self.__requested_function = "DAILY" # Returns only the last 100 data points unless we add another url parameter
            self.__key_name = "Time Series (Daily)"
        elif requested_function == 3:
            self.__requested_function = "WEEKLY"
            self.__key_name = "Weekly Time Series"
        else:
            self.__requested_function = "MONTHLY"
            self.__key_name = "Monthly Time Series"

        # Set url based on requested function
        if self.__requested_function == "INTRADAY":
            self.__URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_{self.__requested_function}&symbol={self.__stock_symbol}&interval={self.__interval}&apikey={self.__API_KEY}"
        else:
            self.__URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_{self.__requested_function}&symbol={self.__stock_symbol}&apikey={self.__API_KEY}"

    def get_data(self):
        get_request = requests.get(self.__URL)
        data_dictionary = get_request.json()
        return data_dictionary[self.__key_name]