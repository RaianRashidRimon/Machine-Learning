#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bokeh.plotting import figure, show
from bokeh.io import output_notebook

# Data
fruits = ['Apple', 'Orange', 'Banana', 'Kiwifruit', 'Blueberry', 'Grapes']
people = [35, 30, 10, 25, 40, 5]

# Create figure
p = figure(x_range=fruits, title="Survey Results: Nicest Fruit", toolbar_location=None, tools="")
p.vbar(x=fruits, top=people, width=0.9, color="skyblue")

p.xaxis.axis_label = "Fruit"
p.yaxis.axis_label = "Number of People"
p.xaxis.major_label_orientation = "vertical"

# Show plot
output_notebook()
show(p)


# In[ ]:




