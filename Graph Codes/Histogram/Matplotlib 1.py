import matplotlib.pyplot as plt

bins = [100, 150, 200, 250, 300, 350] 
frequencies = [5, 12, 15, 10, 3]  




plt.figure(figsize=(10, 6))
plt.hist(bins[:-1], bins, weights=frequencies, edgecolor='black')
plt.title('Tree Heights in Orchard')
plt.xlabel('Height (cm)')
plt.ylabel('Number of Trees')
plt.xticks(bins)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
