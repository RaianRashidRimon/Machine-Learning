from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

minutes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
people = [6, 2, 3, 5, 2, 5, 0, 0, 2, 3, 7, 4, 1]
source = ColumnDataSource(data=dict(minutes=minutes, people=people))
p = figure(width=600, height=400, 
          title="Time to Eat Breakfast Survey",
          x_axis_label='Minutes',
          y_axis_label='Number of People')
p.circle('minutes', 'people', size=10, source=source, alpha=0.6)




p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = "gray"
p.ygrid.grid_line_dash = [6, 4]
p.xaxis.ticker = minutes 




show(p)
