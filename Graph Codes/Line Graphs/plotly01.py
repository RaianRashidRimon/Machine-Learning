import plotly.graph_objects as go

# Data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sales = [410, 440, 550, 420, 610, 790, 770]

# Create line graph
fig = go.Figure(data=[go.Scatter(
    x=days,
    y=sales,
    mode='lines+markers',
    marker=dict(size=8),
    hoverinfo='x+y',
    line=dict(color='blue')
)])

fig.update_layout(
    title='Ice Cream Sales by Day',
    xaxis_title='Day of Week',
    yaxis_title='Sales ($)',
    showlegend=False
)

# Add grid lines
fig.update_xaxes(showgrid=True)
fig.update_yaxes(showgrid=True)

fig.show()
