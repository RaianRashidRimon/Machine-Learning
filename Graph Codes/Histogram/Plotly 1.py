import plotly.graph_objects as go


bins = [100, 150, 200, 250, 300, 350] 
frequencies = [5, 12, 15, 10, 3]  





fig = go.Figure(data=[go.Bar(
    x=[125, 175, 225, 275, 325],  
    y=frequencies,
    width=50,
    marker=dict(line=dict(color='black', width=1))
)])
fig.update_layout(
    title='Tree Heights in Orchard',
    xaxis_title='Height (cm)',
    yaxis_title='Number of Trees',
    bargap=0,  
    xaxis=dict(tickmode='array', tickvals=bins),
    showlegend=False
)
fig.update_yaxes(showgrid=True)
fig.show()
