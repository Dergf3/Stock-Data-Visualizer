def get_chart_type():
    while(True):
        print("\nChart Types")
        print("--------------")
        print("1. Bar")
        print("2. Line\n")
        try:
            chart_type = int(input("Enter the chart type you want (1, 2): "))
            if chart_type == 1 or chart_type == 2:
                return chart_type
                break
            else:
                print("\nEnter a 1 or 2 for chart type")
                continue
        except:
            print("\nEnter a 1 or 2 for chart type")
            continue

def get_time_series():
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
                return time_series
                break
            else:
                print("\nEnter a 1, 2, 3, or 4 for time series")
                continue
        except:
            print("\nEnter a 1, 2, 3, or 4 for time series")
            continue

def main():
    print("Stock Data Visualizer")
    print("------------------------")
    while(True):
        stock_symbol = input("\nEnter the stock symbol you are looking for: ")
        chart = get_chart_type()
        time_s = get_time_series()

        #Start Date
        while(True):
            try:
                date_input = input("Enter the start Date (YYYY-MM-DD): ")
                year, month, day = date_input.split("-")
                year = int(year)
                month = int(month)
                day = int(day)
            
                if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
                    total_days = 31
                elif month == 4 or month == 6 or month == 9 or month == 11:
                    total_days = 30
                elif year%4 == 0 and year%100 != 0 or year % 400 == 0:
                    total_days = 29
                else:
                    total_days = 28    

                if month < 1 or month > 12:
                    print("Invalid month. Please try again")
                    continue
                elif day < 1 or day > total_days:
                    print("Invalid day. Please try again")
                    continue
            except ValueError:
                print("Invalid value. Please try again")
                continue
            else:
                break

        #End Date
        while(True):
            try:
                date_input_2 = input("Enter the end date (YYYY-MM-DD): ")
                YEAR, MONTH, DAY = date_input_2.split("-")
                YEAR = int(YEAR)
                MONTH = int(MONTH)
                DAY = int(DAY)

                if MONTH == 1 or MONTH == 3 or MONTH == 5 or MONTH == 7 or MONTH == 8 or MONTH == 10:
                    total_days_2 = 31
                elif MONTH == 4 or MONTH == 6 or MONTH == 9 or MONTH == 11:
                    total_days_2 = 30
                elif YEAR % 4 == 0 and YEAR % 100 != 0 or YEAR % 400 == 0:
                    total_days_2 = 29
                else:
                    total_days_2 = 28
                
                if MONTH < 1 or MONTH > 12:
                    print("Invalid month. Please try again")
                    continue
                elif DAY < 1 or DAY > total_days_2:
                    print("Invalid day. Please try again")
                    continue
                elif YEAR < year:
                    print("Start date cannot be later than End date. Please enter the date again")
                    continue
                elif YEAR >= year and MONTH < month:
                    print("Start date cannont be later than End date. Please enter the date again")
                    continue
                elif YEAR == year and MONTH == month and DAY < day:
                    print("Start date cannont be later than End date. Please enter the date again")
                    continue
            except ValueError:
                print("Invalid value. Please try again")
                continue
            else:
                break
        
        print(stock_symbol)
        print(chart)
        print(time_s)
        print(date_input)
        print(date_input_2)


        ask = input("\nWould you like to view more stock data? Press 'y' to continue: ")
        if ask != "y":
            print("Thank You. Goodbye!")
            break
        else:
            continue

main()
        
