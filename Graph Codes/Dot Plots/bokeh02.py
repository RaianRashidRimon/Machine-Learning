from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# Data
percent_access = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
countries = [5, 6, 12, 5, 4, 5, 6, 10, 15, 34]

# Create data source
source = ColumnDataSource(data=dict(percent=percent_access, countries=countries))

# Create figure
p = figure(width=600, height=400,
          title="Access to Electricity by Country",
          x_axis_label='Percentage of Population with Access (%)',
          y_axis_label='Number of Countries')

# Add dots
p.circle('percent', 'countries', size=10, source=source, color='blue', alpha=0.6)

# Customize
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = "gray"
p.ygrid.grid_line_dash = [6, 4]

show(p)
