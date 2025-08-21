from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource

# Data
months = ['March', 'April', 'May', 'June', 'July', 'August']
cumulative = [120, 170, 280, 380, 430, 450]

# Create data source
source = ColumnDataSource(data=dict(months=months, cumulative=cumulative))

# Create figure for bar graph
bar_fig = figure(width=400, height=400,
                 title="Cumulative Earnings (Bar Graph)",
                 x_axis_label='Month',
                 y_axis_label='Cumulative Earnings ($)',
                 x_range=months)
bar_fig.vbar(x='months', top='cumulative', width=0.5, source=source, fill_color='lightblue', line_color='black')

# Create figure for line graph
line_fig = figure(width=400, height=400,
                  title="Cumulative Earnings (Line Graph)",
                  x_axis_label='Month',
                  y_axis_label='Cumulative Earnings ($)',
                  x_range=months)
line_fig.line('months', 'cumulative', source=source, color='green', line_width=2, legend_label='Cumulative Earnings')
line_fig.scatter('months', 'cumulative', source=source, size=8, color='green', legend_label='Data Points')
line_fig.legend.click_policy="hide"

# Arrange figures in a 1x2 grid
grid = gridplot([[bar_fig, line_fig]])

show(grid)
