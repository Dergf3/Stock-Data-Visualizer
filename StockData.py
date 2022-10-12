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

        if requested_function == 1:
            self.__requested_function = "INTRADAY"
        elif requested_function == 2:
            self.__requested_function = "DAILY"
        elif requested_function == 3:
            self.__requested_function = "WEEKLY"
        else:
            self.__requested_function = "MONTHLY"

        self.__URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_{self.__requested_function}&symbol={self.__stock_symbol}&apikey={self.__API_KEY}"

    def get_data(self):
        get_request = requests.get(self.__URL)
        self.data_dictionary = get_request.json()