from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

bins = [100, 150, 200, 250, 300, 350] 
frequencies = [5, 12, 15, 10, 3]
hist_data = dict(
    left=[100, 150, 200, 250, 300],
    right=[150, 200, 250, 300, 350],
    top=frequencies
)
source = ColumnDataSource(data=hist_data)
p = figure(width=600, height=400,
          title="Tree Heights in Orchard",
          x_axis_label='Height (cm)',
          y_axis_label='Number of Trees')
p.quad(left='left', right='right', top='top', bottom=0, source=source,
       fill_color='skyblue', line_color='black')




p.xaxis.ticker = bins
p.ygrid.grid_line_color = "gray"
p.ygrid.grid_line_dash = [6, 4]
p.xgrid.grid_line_color = None
show(p)
