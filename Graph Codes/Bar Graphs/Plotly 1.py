import plotly.express as px

fruits = ['Apple', 'Orange', 'Banana', 'Kiwifruit', 'Blueberry', 'Grapes']
people = [35, 30, 10, 25, 40, 5]
fig = px.bar(x=fruits, y=people, labels={'x': 'Fruit', 'y': 'Number of People'}, title='Survey Results: Nicest Fruit')
fig.show()
