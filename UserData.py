class UserData:
    def __init__(self):
        self.stock_symbol = input("\nEnter the stock symbol you are looking for: ")
        self.chart_type = self.get_chart_type()
        self.requested_function = self.get_time_series()
        self.start_date = self.get_valid_date()
        self.end_date = self.get_valid_date("end", self.start_date)

    def get_chart_type(self):
        chart_type = 0
        while(True):
            print("\nChart Types")
            print("--------------")
            print("1. Bar")
            print("2. Line\n")
            try:
                chart_type = int(input("Enter the chart type you want (1, 2): "))
                if chart_type == 1 or chart_type == 2:
                    break
                else:
                    print("\nEnter a 1 or 2 for chart type")
                    continue
            except:
                print("\nEnter a 1 or 2 for chart type")
                continue
        return chart_type

    def get_time_series(self):
        time_series = 0
        while(True):
            print("\nSelect the Time Series of the chart you want to Generate:")
            print("---------------------------------------------------------")
            print("1. Intraday")
            print("2. Daily")
            print("3. Weekly")
            print("4. Monthly\n")
            try:
                time_series = int(input("Enter the time series option (1, 2, 3, 4): "))
                if time_series == 1 or time_series == 2 or time_series == 3 or time_series == 4:
                    break
                else:
                    print("\nEnter a 1, 2, 3, or 4 for time series")
                    continue
            except:
                print("\nEnter a 1, 2, 3, or 4 for time series")
                continue
        return time_series

    def get_integer(self, date_str):
        try:
            year, month, day = date_str.split("-")
            year = int(year)
            month = int(month)
            day = int(day)
            
        except:
            raise ValueError("Invalid date. Please try again")
            
        else:
            return (year, month, day)

    def get_valid_date(self, date_name = "start", start_date = ""):
        while(True):
            date_input = input(f"Enter the {date_name} date (YYYY-MM-DD): ")
            try:
                year, month, day = self.get_integer(date_input)
            except ValueError as ex:
                print(ex)
                continue
            else:  
                if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
                    total_days = 31
                elif month == 4 or month == 6 or month == 9 or month == 11:
                    total_days = 30
                elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                    total_days = 29
                else:
                    total_days = 28
                        
                if month < 1 or month > 12:
                    print("Invalid month. Please try again")
                    continue
                elif day < 1 or day > total_days:
                    print("Invalid date. Please try again")
                    continue
                
                if date_name == "end":
                    try:
                        end_year, end_month, end_day = self.get_integer(start_date)
                    except ValueError as ex:
                        print(ex)
                        continue
                    else:
                        if end_year < year:
                            print("Start date cannot be later than End date. Please enter the date again")
                            continue
                        elif end_year == year and end_month < month:
                            print("Start date cannot be later than End date. Please enter the date again")
                            continue
                        elif end_year == year and end_month == month and end_day > day:
                            print("Start date cannot be later than End date. Please enter the date again")
                            continue
                        else:
                            break
                else:
                    break
        return date_input

