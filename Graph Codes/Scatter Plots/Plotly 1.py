import plotly.graph_objects as go
import numpy as np
from sklearn.linear_model import LinearRegression

temperatures = np.array([14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2])
sales = np.array([215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408])
model = LinearRegression()
model.fit(temperatures.reshape(-1, 1), sales)
temp_range = np.linspace(min(temperatures), max(temperatures), 100)
sales_pred = model.predict(temp_range.reshape(-1, 1))
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=temperatures,
    y=sales,
    mode='markers',
    name='Data Points',
    marker=dict(color='blue', size=8)
))
fig.add_trace(go.Scatter(
    x=temp_range,
    y=sales_pred,
    mode='lines',
    name='Best-Fit Line',
    line=dict(color='red', width=2)
))
fig.update_layout(
    title='Ice Cream Sales vs. Temperature',
    xaxis_title='Temperature (°C)',
    yaxis_title='Ice Cream Sales ($)',
    showlegend=True
)
fig.update_xaxes(showgrid=True)
fig.update_yaxes(showgrid=True)
fig.show()





print(f'Best-Fit Line: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}')
