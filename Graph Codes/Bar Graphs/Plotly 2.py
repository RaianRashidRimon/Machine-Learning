import plotly.express as px

# Data
grades = ['A', 'B', 'C', 'D']
students = [4, 12, 10, 2]

# Plot
fig = px.bar(x=grades, y=students, labels={'x': 'Grade', 'y': 'Number of Students'}, title='Test Results')
fig.show()
