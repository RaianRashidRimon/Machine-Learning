import plotly.graph_objects as go



weight_gains = [-0.2, 0, 0.1, 0.1, 0.3, 0.4, 0.5, 0.5, 0.6, 1.6]
bins = [-0.5, 0, 0.5, 1.0, 1.5, 2.0]




fig = go.Figure(data=[go.Histogram(
    x=weight_gains,
    xbins=dict(start=-0.5, end=2.0, size=0.5),
    marker=dict(
        color='green',
        line=dict(color='black', width=1)
    )
)])
fig.update_layout(
    title='Pup Weight Gain per Month',
    xaxis_title='Weight Gain (kg)',
    yaxis_title='Number of Months',
    xaxis=dict(tickmode='array', tickvals=bins),
    bargap=0,
    showlegend=False
)
fig.update_yaxes(showgrid=True)
fig.show()
