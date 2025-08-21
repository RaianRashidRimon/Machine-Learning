

from bokeh.plotting import figure, show
from bokeh.io import output_notebook

# Data
grades = ['A', 'B', 'C', 'D']
students = [4, 12, 10, 2]

# Create figure
p = figure(x_range=grades, title="Test Results", toolbar_location=None, tools="")
p.vbar(x=grades, top=students, width=0.9, color="lightgreen")

# Labels
p.xaxis.axis_label = "Grade"
p.yaxis.axis_label = "Number of Students"
p.xaxis.major_label_orientation = "vertical"

# Show plot
output_notebook()
show(p)





