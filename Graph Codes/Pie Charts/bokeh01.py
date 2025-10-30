#!/usr/bin/env python
# coding: utf-8

# In[5]:


from bokeh.palettes import Category20
from bokeh.plotting import figure, show
from bokeh.transform import cumsum
from math import pi
import pandas as pd

# Data
data = pd.Series({
    'Comedy': 4,
    'Action': 5,
    'Romance': 6,
    'Drama': 1,
    'SciFi': 4
})

# Prepare data
data = data.reset_index(name='value')
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20[len(data)]

# Create figure
p = figure(height=400, title="Favorite Movie Genres", 
          toolbar_location=None, tools="hover", 
          tooltips="@index: @value", x_range=(-0.5, 1.0))

# Add pie wedges
p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), 
        end_angle=cumsum('angle'),
        line_color="white", fill_color='color', 
        legend_field='index', source=data)

# Customize
p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None

show(p)


# In[ ]:




