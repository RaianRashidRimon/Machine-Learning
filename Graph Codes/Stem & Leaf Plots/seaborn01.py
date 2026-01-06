import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Data
stems = [2, 3, 4, 5]  # Stems from the data
leaves = [[3, 5, 5, 7, 8], [2, 6, 6], [5], [0]]  # Leaves for each stem

# Flatten data for plotting
all_leaves = []
all_stems = []
for stem, leaf_list in zip(stems, leaves):
    all_leaves.extend(leaf_list)
    all_stems.extend([stem] * len(leaf_list))

# Create scatter plot with Seaborn styling
plt.figure(figsize=(10, 6))
sns.scatterplot(x=all_leaves, y=all_stems, s=100, color='blue')
plt.title("Stem-and-Leaf Plot of Long Jump Distances (meters)")
plt.xlabel('Leaf (Tenths Place)')
plt.ylabel('Stem (Whole Number)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.yticks(stems)  # Show only the stem values
plt.show()
