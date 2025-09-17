import matplotlib.pyplot as plt

weight_gains = [-0.2, 0, 0.1, 0.1, 0.3, 0.4, 0.5, 0.5, 0.6, 1.6]
bins = [-0.5, 0, 0.5, 1.0, 1.5, 2.0]




plt.figure(figsize=(10, 6))
plt.hist(weight_gains, bins=bins, edgecolor='green', color='green') 
plt.title('Pup Weight Gain per Month')
plt.xlabel('Weight Gain (kg)')
plt.ylabel('Number of Months')
plt.xticks(bins)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
