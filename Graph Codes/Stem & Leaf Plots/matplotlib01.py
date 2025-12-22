import matplotlib.pyplot as plt

# Data (organized by stem)
stems = [2, 3, 4, 5]  # Stems from the data
leaves = [[3, 5, 5, 7, 8], [2, 6, 6], [5], [0]]  # Leaves for each stem

# Create stem plot
plt.figure(figsize=(10, 6))
for i, (stem, leaf_list) in enumerate(zip(stems, leaves)):
    # Position leaves along the stem
    y_positions = [stem] * len(leaf_list)
    plt.stem(leaf_list, y_positions, linefmt='C0-', markerfmt='C0o', basefmt='C0-')

plt.title("Stem-and-Leaf Plot of Long Jump Distances (meters)")
plt.xlabel('Leaf (Tenths Place)')
plt.ylabel('Stem (Whole Number)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
