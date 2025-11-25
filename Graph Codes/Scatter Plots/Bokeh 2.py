from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, LabelSet
import numpy as np
from sklearn.linear_model import LinearRegression

countries = ['Madagascar', 'India', 'Mexico', 'Taiwan', 'Norway']
production = [800, 3100, 9600, 25300, 40000]
birth_rate = [5.70, 2.85, 2.49, 1.57, 1.78]




model = LinearRegression()
model.fit(np.array(production).reshape(-1, 1), birth_rate)
prod_range = np.linspace(min(production), max(production), 100)
birth_pred = model.predict(prod_range.reshape(-1, 1))




source = ColumnDataSource(data=dict(production=production, birth_rate=birth_rate, countries=countries))
line_source = ColumnDataSource(data=dict(production=prod_range, birth_rate=birth_pred))



p = figure(width=600, height=400,
          title="Yearly Production per Person vs. Birth Rate by Country",
          x_axis_label='Yearly Production per Person ($)',
          y_axis_label='Birth Rate (per woman)')
p.scatter('production', 'birth_rate', source=source, size=10, color='blue', legend_label='Data Points')
p.line('production', 'birth_rate', source=line_source, color='red', legend_label='Best-Fit Line')
labels = LabelSet(x='production', y='birth_rate', text='countries', source=source,
                 x_offset=5, y_offset=5, text_font_size='8pt')
p.add_layout(labels)
p.grid.grid_line_color = "gray"
p.grid.grid_line_dash = [6, 4]
p.legend.click_policy="hide"
show(p)


print(f'Best-Fit Line: y = {model.coef_[0]:.4f}x + {model.intercept_:.4f}')
