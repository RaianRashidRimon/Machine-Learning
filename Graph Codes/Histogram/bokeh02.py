from bokeh.plotting import figure, show
import numpy as np

# Data
weight_gains = [-0.2, 0, 0.1, 0.1, 0.3, 0.4, 0.5, 0.5, 0.6, 1.6]
bins = [-0.5, 0, 0.5, 1.0, 1.5, 2.0]

# Calculate histogram
hist, edges = np.histogram(weight_gains, bins=bins)

# Create figure
p = figure(width=600, height=400,
          title="Pup Weight Gain per Month",
          x_axis_label='Weight Gain (kg)',
          y_axis_label='Number of Months')

# Add bars
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
       fill_color='green', line_color='black')  # Changed to green

# Customize
p.xaxis.ticker = bins
p.ygrid.grid_line_color = "gray"
p.ygrid.grid_line_dash = [6, 4]
p.xgrid.grid_line_color = None

show(p)
