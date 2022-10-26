import pygal
def bar_func():
    bar_chart.title = 'Stock Data For' + stock_symbol
    bar_chart = pygal.Bar()
    bar_chart.x_labels = map(str, range(year, YEAR))
    bar_chart.add('Open', [])
    bar_chart.add('High',  [])
    bar_chart.add('Low',      [])
    bar_chart.add('CLose',  [])
    bar_chart.render_in_browser()