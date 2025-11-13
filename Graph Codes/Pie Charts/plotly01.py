import plotly.graph_objects as go

# Data
movies = ['Comedy', 'Action', 'Romance', 'Drama', 'SciFi']
votes = [4, 5, 6, 1, 4]

# Plot
fig = go.Figure(data=[go.Pie(labels=movies, values=votes, hole=0.3)])
fig.update_layout(title='Favorite Type of Movie')
fig.show()
