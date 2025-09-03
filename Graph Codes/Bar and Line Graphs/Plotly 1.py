import plotly.graph_objects as go
import numpy as np

# Data
months = ['March', 'April', 'May', 'June', 'July', 'August']
cumulative = [120, 170, 280, 380, 430, 450]

# Create figure with both bar and line traces
fig = go.Figure()

# Add cumulative bar graph
fig.add_trace(go.Bar(
    x=months,
    y=cumulative,
    name='Cumulative Earnings (Bar)',
    marker=dict(color='lightblue', line=dict(color='black', width=1))
))

# Add cumulative line graph
fig.add_trace(go.Scatter(
    x=months,
    y=cumulative,
    mode='lines+markers',
    name='Cumulative Earnings (Line)',
    marker=dict(color='green', size=8),
    line=dict(color='green', width=2)
))

fig.update_layout(
    title='Cumulative Earnings by Month',
    xaxis_title='Month',
    yaxis_title='Cumulative Earnings ($)',
    barmode='group',
    showlegend=True
)

# Add grid lines
fig.update_xaxes(showgrid=True)
fig.update_yaxes(showgrid=True)

# Rotate x-axis labels for readability
fig.update_layout(xaxis=dict(tickangle=45))

fig.show()
