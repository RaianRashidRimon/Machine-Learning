import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

months = ['March', 'April', 'May', 'June', 'July', 'August']
cumulative = [120, 170, 280, 380, 430, 450]
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.barplot(x=months, y=cumulative, color='lightblue')
plt.title('Cumulative Earnings (Bar Graph)')
plt.xlabel('Month')
plt.ylabel('Cumulative Earnings ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.subplot(1, 2, 2)
sns.lineplot(x=months, y=cumulative, marker='o', color='green')
plt.title('Cumulative Earnings (Line Graph)')
plt.xlabel('Month')
plt.ylabel('Cumulative Earnings ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)




plt.tight_layout()
plt.show()
