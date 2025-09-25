import matplotlib.pyplot as plt


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sales = [410, 440, 550, 420, 610, 790, 770]



plt.figure(figsize=(10, 6))
plt.plot(days, sales, marker='o', linestyle='-', color='b')
plt.title('Ice Cream Sales by Day')
plt.xlabel('Day of Week')
plt.ylabel('Sales ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
