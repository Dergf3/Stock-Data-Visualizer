def chart(self):
    print("User Data chart type: ", self.user_data.chart_type)
    if self.user_data.chart_type == 1:
        chart = pygal.Bar(x_label_rotation=45)
    else:
        chart = pygal.Line(x_label_rotation=45)
    chart.title =title=f"Stock data for {self.user_data.stock_symbol} stocks for {self.user_data.start_date} to {self.user_data.end_date}"
    self.date_list.reverse()
    chart.x_labels = self.date_list
    chart.add("Open", self.open_list)
    chart.add("Close", self.close_list)
    chart.add("Low", self.low_list)
    chart.add("High", self.hugh_list)
    chart.render_in_browser()
    
