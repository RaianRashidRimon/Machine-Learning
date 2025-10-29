import plotly.graph_objects as go

# Data
months = ['January', 'February', 'March', 'April']
apples = [10, 40, 25, 20]
apple_counts = [a / 10 for a in apples]

# Text labels for apple symbols
apple_labels = ['🍎' * int(c) + ('½🍎' if c % 1 >= 0.5 else '') for c in apple_counts]

# Create bar plot
fig = go.Figure(data=[go.Bar(
    x=months,
    y=apple_counts,
    text=apple_labels,
    textposition='auto',
    marker=dict(color='red')
)])

fig.update_layout(
    title='Apple Sales by Month',
    xaxis_title='Month',
    yaxis_title='Number of Apples (1 🍎 = 10 apples)',
    yaxis=dict(range=[0, 5]),
    showlegend=False
)

fig.update_yaxes(showgrid=True)
fig.show()
