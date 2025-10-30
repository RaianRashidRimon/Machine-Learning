import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Segoe UI Emoji', 'Apple Color Emoji', 'DejaVu Sans']

# Data
months = ['January', 'February', 'March', 'April']
apples = [10, 40, 25, 20]
apple_counts = [a / 10 for a in apples]

# Create bar plot with red bars
plt.figure(figsize=(10, 6))
ax = sns.barplot(x=months, y=apple_counts, color='red')

plt.title('Apple Sales by Month')
plt.xlabel('Month')
plt.ylabel('Number of Apples (1 🍎 = 10 apples)')
plt.ylim(0, 5)

# Add apple symbols
for i, count in enumerate(apple_counts):
    label = '🍎' * int(count) + ('½🍎' if count % 1 >= 0.5 else '')
    ax.text(i, count, label, ha='center', va='bottom')

plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()
