import plotly.graph_objects as go
import numpy as np
stems = [2, 3, 4, 5]
leaves = [[3, 5, 5, 7, 8], [2, 6, 6], [5], [0]]
all_leaves = []
all_stems = []
for stem, leaf_list in zip(stems, leaves):
    all_leaves.extend(leaf_list)
    all_stems.extend([stem] * len(leaf_list))
fig = go.Figure(data=[go.Scatter(
    x=all_leaves,
    y=all_stems,
    mode='markers',
    marker=dict(size=10, color='blue'),
    text=[f'Stem {stem}, Leaf {leaf}' for stem, leaf in zip(all_stems, all_leaves)],
    hoverinfo='text+x+y'
)])



fig.update_layout(
    title='Stem-and-Leaf Plot of Long Jump Distances (meters)',
    xaxis_title='Leaf (Tenths Place)',
    yaxis_title='Stem (Whole Number)',
    yaxis=dict(tickmode='array', tickvals=stems),
    showlegend=False
)
fig.update_xaxes(showgrid=True)
fig.update_yaxes(showgrid=True)
fig.show()
