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
        self.API_KEY = "EYRT2L2R3HI4L78O"
        self.stock_symbol = stock_symbol

        if requested_function == 1:
            self.requested_function = "INTRADAY"
        elif requested_function == 2:
            self.requested_function = "DAILY"
        elif requested_function == 3:
            self.requested_function = "WEEKLY"
        else:
            self.requested_function = "MONTHLY"

        self.URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_{self.requested_function}&symbol={self.stock_symbol}&apikey={self.API_KEY}"

    def get_data(self):
        get_request = requests.get(self.URL)
        self.data_dictionary = get_request.json()