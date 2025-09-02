import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['March', 'April', 'May', 'June', 'July', 'August']
cumulative = [120, 170, 280, 380, 430, 450]

# Create figure with two subplots side by side
plt.figure(figsize=(12, 5))

# Cumulative Bar Graph (left subplot)
plt.subplot(1, 2, 1)
plt.bar(months, cumulative, color='lightblue', edgecolor='black')
plt.title('Cumulative Earnings (Bar Graph)')
plt.xlabel('Month')
plt.ylabel('Cumulative Earnings ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)

# Cumulative Line Graph (right subplot)
plt.subplot(1, 2, 2)
plt.plot(months, cumulative, marker='o', color='green', linestyle='-', linewidth=2)
plt.title('Cumulative Earnings (Line Graph)')
plt.xlabel('Month')
plt.ylabel('Cumulative Earnings ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
