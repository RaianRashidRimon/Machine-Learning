from bokeh.palettes import Category20
from bokeh.plotting import figure, show
from bokeh.transform import cumsum
from math import pi
import pandas as pd
data = pd.Series({
    'A': 4,
    'B': 12,
    'C': 10,
    'D': 2
})
data = data.reset_index(name='value')
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20[len(data)]
p = figure(height=400, title="Grade Distribution in Recent Test",
          toolbar_location=None, tools="hover",
          tooltips="@index: @value", x_range=(-0.5, 1.0))
p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True),
        end_angle=cumsum('angle'),
        line_color="white", fill_color='color',
        legend_field='index', source=data)
p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None
show(p)
