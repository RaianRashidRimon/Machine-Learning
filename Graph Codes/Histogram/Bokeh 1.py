from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# Data
bins = [100, 150, 200, 250, 300, 350]  # Bin edges
frequencies = [5, 12, 15, 10, 3]  # Example frequencies

# Prepare data
hist_data = dict(
    left=[100, 150, 200, 250, 300],
    right=[150, 200, 250, 300, 350],
    top=frequencies
)
source = ColumnDataSource(data=hist_data)

# Create figure
p = figure(width=600, height=400,
          title="Tree Heights in Orchard",
          x_axis_label='Height (cm)',
          y_axis_label='Number of Trees')

# Add bars
p.quad(left='left', right='right', top='top', bottom=0, source=source,
       fill_color='skyblue', line_color='black')

# Customize
p.xaxis.ticker = bins
p.ygrid.grid_line_color = "gray"
p.ygrid.grid_line_dash = [6, 4]
p.xgrid.grid_line_color = None

show(p)
