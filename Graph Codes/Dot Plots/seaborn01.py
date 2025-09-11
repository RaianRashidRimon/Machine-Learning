import seaborn as sns
import matplotlib.pyplot as plt

# Data
minutes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
people = [6, 2, 3, 5, 2, 5, 0, 0, 2, 3, 7, 4, 1]

# Create dot plot with seaborn styling
plt.figure(figsize=(10, 6))
sns.scatterplot(x=minutes, y=people, size=100, sizes=(100, 100), alpha=0.6)
plt.title('Time to Eat Breakfast Survey')
plt.xlabel('Minutes')
plt.ylabel('Number of People')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(minutes)
plt.show()
