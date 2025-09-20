import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate data points based on assumed frequencies
heights = (np.array([125] * 5 + [175] * 12 + [225] * 15 + [275] * 10 + [325] * 3))
bins = [100, 150, 200, 250, 300, 350]

# Create histogram with seaborn styling
plt.figure(figsize=(10, 6))
sns.histplot(data=heights, bins=bins, edgecolor='black')
plt.title('Tree Heights in Orchard')
plt.xlabel('Height (cm)')
plt.ylabel('Number of Trees')
plt.xticks(bins)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
