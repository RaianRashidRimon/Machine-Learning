import plotly.graph_objects as go
grades = ['A', 'B', 'C', 'D']
counts = [4, 12, 10, 2]
fig = go.Figure(data=[go.Pie(labels=grades,
                            values=counts,
                            textinfo='percent+label',
                            hole=0)]) 
fig.update_layout(title_text='Grade Distribution in Recent Test')
fig.show()
