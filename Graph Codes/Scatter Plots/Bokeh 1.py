from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
import numpy as np
from sklearn.linear_model import LinearRegression

temperatures = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2]
sales = [215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408]
model = LinearRegression()
model.fit(np.array(temperatures).reshape(-1, 1), sales)




temp_range = np.linspace(min(temperatures), max(temperatures), 100)
sales_pred = model.predict(temp_range.reshape(-1, 1))
source = ColumnDataSource(data=dict(temp=temperatures, sales=sales))
line_source = ColumnDataSource(data=dict(temp=temp_range, sales=sales_pred))
p = figure(width=600, height=400,
          title="Ice Cream Sales vs. Temperature",
          x_axis_label='Temperature (°C)',
          y_axis_label='Ice Cream Sales ($)')

p.scatter('temp', 'sales', source=source, size=8, color='blue', legend_label='Data Points')
p.line('temp', 'sales', source=line_source, color='red', legend_label='Best-Fit Line')
p.grid.grid_line_color = "gray"
p.grid.grid_line_dash = [6, 4]
p.legend.click_policy="hide"
show(p)
print(f'Best-Fit Line: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}')
