import seaborn as sns
import matplotlib.pyplot as plt

# Data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sales = [410, 440, 550, 420, 610, 790, 770]

# Create line graph with seaborn styling
plt.figure(figsize=(10, 6))
sns.lineplot(x=days, y=sales, marker='o')
plt.title('Ice Cream Sales by Day')
plt.xlabel('Day of Week')
plt.ylabel('Sales ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
