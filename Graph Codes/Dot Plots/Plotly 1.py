import plotly.graph_objects as go

minutes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
people = [6, 2, 3, 5, 2, 5, 0, 0, 2, 3, 7, 4, 1]






fig = go.Figure(data=[go.Scatter(
    x=minutes,
    y=people,
    mode='markers',
    marker=dict(size=12),
    text=[f'{p} people' for p in people],
    hoverinfo='x+y+text'
)])
fig.update_layout(
    title='Time to Eat Breakfast Survey',
    xaxis_title='Minutes',
    yaxis_title='Number of People',
    xaxis=dict(tickmode='array', tickvals=minutes),
    showlegend=False
)
fig.update_xaxes(showgrid=True)
fig.update_yaxes(showgrid=True)
fig.show()
