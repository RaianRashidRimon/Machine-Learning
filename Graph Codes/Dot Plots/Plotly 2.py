import plotly.graph_objects as go

# Data
percent_access = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
countries = [5, 6, 12, 5, 4, 5, 6, 10, 15, 34]

# Create dot plot
fig = go.Figure(data=[go.Scatter(
    x=percent_access,
    y=countries,
    mode='markers',
    marker=dict(size=12),
    text=[f'{c} countries' for c in countries],
    hoverinfo='x+y+text'
)])

fig.update_layout(
    title='Access to Electricity by Country',
    xaxis_title='Percentage of Population with Access (%)',
    yaxis_title='Number of Countries',
    xaxis=dict(tickmode='array', tickvals=percent_access),
    showlegend=False
)

# Add grid lines
fig.update_xaxes(showgrid=True)
fig.update_yaxes(showgrid=True)

fig.show()
