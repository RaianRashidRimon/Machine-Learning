from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

stems = [2, 3, 4, 5]
leaves = [[3, 5, 5, 7, 8], [2, 6, 6], [5], [0]]
all_leaves = []
all_stems = []
for stem, leaf_list in zip(stems, leaves):
    all_leaves.extend(leaf_list)
    all_stems.extend([stem] * len(leaf_list))
source = ColumnDataSource(data=dict(leaves=all_leaves, stems=all_stems))
p = figure(width=600, height=400,
          title="Stem-and-Leaf Plot of Long Jump Distances (meters)",
          x_axis_label='Leaf (Tenths Place)',
          y_axis_label='Stem (Whole Number)',
          y_range=[1.5, 5.5])  



p.scatter('leaves', 'stems', source=source, size=10, color='blue')
p.xgrid.grid_line_color = "gray"
p.xgrid.grid_line_dash = [6, 4]
p.ygrid.grid_line_color = None
p.yaxis.ticker = stems  
show(p)
