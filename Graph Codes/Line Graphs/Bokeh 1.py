from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sales = [410, 440, 550, 420, 610, 790, 770]

source = ColumnDataSource(data=dict(days=days, sales=sales))
p = figure(width=600, height=400,
          title="Ice Cream Sales by Day",
          x_axis_label='Day of Week',
          y_axis_label='Sales ($)',
          x_range=days)
p.line('days', 'sales', source=source, line_width=2, color='blue')
p.circle('days', 'sales', source=source, size=8, fill_color='white', line_color='blue')



p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = "gray"
p.ygrid.grid_line_dash = [6, 4]
show(p)
