import plotly.graph_objects as go
import numpy as np
from sklearn.linear_model import LinearRegression

# Data
countries = ['Madagascar', 'India', 'Mexico', 'Taiwan', 'Norway']
production = np.array([800, 3100, 9600, 25300, 40000])
birth_rate = np.array([5.70, 2.85, 2.49, 1.57, 1.78])

# Fit linear regression
model = LinearRegression()
model.fit(production.reshape(-1, 1), birth_rate)

# Predict values for the line
prod_range = np.linspace(min(production), max(production), 100)
birth_pred = model.predict(prod_range.reshape(-1, 1))

# Create scatter plot
fig = go.Figure()

# Add scatter points with country names in hover
fig.add_trace(go.Scatter(
    x=production,
    y=birth_rate,
    mode='markers',
    name='Data Points',
    marker=dict(color='blue', size=10),
    text=countries,
    hoverinfo='x+y+text'
))

# Add best-fit line
fig.add_trace(go.Scatter(
    x=prod_range,
    y=birth_pred,
    mode='lines',
    name='Best-Fit Line',
    line=dict(color='red', width=2)
))

fig.update_layout(
    title='Yearly Production per Person vs. Birth Rate by Country',
    xaxis_title='Yearly Production per Person ($)',
    yaxis_title='Birth Rate (per woman)',
    showlegend=True
)

# Add grid lines
fig.update_xaxes(showgrid=True)
fig.update_yaxes(showgrid=True)

fig.show()

# Print the equation of the line (optional)
print(f'Best-Fit Line: y = {model.coef_[0]:.4f}x + {model.intercept_:.4f}')
