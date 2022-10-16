import requests
from json import JSONDecodeError
from datetime import datetime

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
        self.__URL = "https://www.alphavantage.co/query"
        self.__stock_symbol = stock_symbol
        self.__params_dictionary = {"symbol" : self.__stock_symbol, "apikey" : self.__API_KEY}
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

        # Set url parameters based on requested function
        self.__params_dictionary.update({"function" : f"TIME_SERIES_{self.__requested_function}"})
        if self.__requested_function == "INTRADAY":
            self.__params_dictionary.update({"interval" : self.__interval})

    def get_data(self, user_start_date: str, user_end_date: str):
        data_dictionary = {}
        try:
            api_response = requests.get(self.__URL, params=self.__params_dictionary)
        except:
            raise Exception("The API is currently unavailable.  Please try again later.  If the problem persists, please contact your system administrator.")
        else:
            if api_response.ok:
                # The API sends a 200 OK response even if there are errors.  If there are errors,
                # it will return them in the response text.  Filter them out by converting the response
                # to a python dictionary and retrieving the "Error Message" key.
                if 'Error Message' in api_response.text:
                    self.__handle_API_response_errors(api_response)
                else:
                    try:
                        data_dictionary = self.__filter_API_response(api_response, user_start_date, user_end_date)
                    except Exception as ex:
                        raise Exception(ex)
            else:
                raise Exception(f"The API responded with status code \"{api_response.status_code}.\"")
        return data_dictionary

    def __handle_API_response_errors(self, api_response):
        try:
            response_dictionary = api_response.json()
        except JSONDecodeError:
            raise Exception("JSON decoding error")
        else:
            error_msg = response_dictionary.get('Error Message')
            if error_msg != None:
                raise Exception(error_msg)

    def __filter_API_response(self, api_response, user_start_date: str, user_end_date: str):
        filtered_dictionary = {}
        # Gets a dictionary with a date string (format:  YYYY-MM-DD) as the key 
        # and dictionary as the value based off of the selected function
        try:            
            response_dictionary = api_response.json()
        except JSONDecodeError:
            raise Exception("JSON decoding error")

        data_dictionary = response_dictionary.get(self.__key_name)
        if data_dictionary != None:
            # Convert to dates for comparison.  This may be risky since it assumes the user's
            # dates have already been verified to be valid and in the correct format.
            try:
                start_date = datetime.strptime(user_start_date, "%Y-%m-%d")
            except ValueError:
                raise Exception(f"{user_start_date} is an invalid date.")

            try:
                end_date = datetime.strptime(user_end_date, "%Y-%m-%d")
            except ValueError:
                raise Exception(f"{user_end_date} is an invalid date.")
            
            for key, value in data_dictionary.items():
                # Convert keys to dates for comparison
                retrieved_date = datetime.strptime(key, "%Y-%m-%d")
                if retrieved_date >= start_date and retrieved_date <= end_date:
                    filtered_dictionary.update({key : value})
        
        else:
            raise Exception("The API keys used for filtering have changed.  Please notify your system administrator to correct this issue.")
        
        return filtered_dictionary