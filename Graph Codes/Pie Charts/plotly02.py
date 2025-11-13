import plotly.graph_objects as go

# Data
grades = ['A', 'B', 'C', 'D']
counts = [4, 12, 10, 2]

# Create pie chart
fig = go.Figure(data=[go.Pie(labels=grades,
                            values=counts,
                            textinfo='percent+label',
                            hole=0)])  # Set hole=0.3 for donut chart if desired
fig.update_layout(title_text='Grade Distribution in Recent Test')
fig.show()
