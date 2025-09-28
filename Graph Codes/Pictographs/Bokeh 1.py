from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, LabelSet

months = ['January', 'February', 'March', 'April']
apples = [10, 40, 25, 20]
apple_counts = [a / 10 for a in apples]
apple_labels = ['🍎' * int(c) + ('½🍎' if c % 1 >= 0.5 else '') for c in apple_counts]
source = ColumnDataSource(data=dict(months=months, counts=apple_counts, labels=apple_labels))





p = figure(width=600, height=400, x_range=months,
          title="Apple Sales by Month",
          x_axis_label='Month',
          y_axis_label='Number of Apples (1 🍎 = 10 apples)')
p.vbar(x='months', top='counts', width=0.5, source=source, fill_color='red')
labels = LabelSet(x='months', y='counts', text='labels', source=source,
                 text_align='center', y_offset=5)
p.add_layout(labels)
p.y_range.start = 0
p.y_range.end = 5
p.ygrid.grid_line_color = "gray"
p.ygrid.grid_line_dash = [6, 4]
p.xgrid.grid_line_color = None
show(p)
