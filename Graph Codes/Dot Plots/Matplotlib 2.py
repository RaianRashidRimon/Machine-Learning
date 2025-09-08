import matplotlib.pyplot as plt

# Data
percent_access = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
countries = [5, 6, 12, 5, 4, 5, 6, 10, 15, 34]

# Create dot plot
plt.figure(figsize=(10, 6))
plt.scatter(percent_access, countries, s=100, alpha=0.6)
plt.title('Access to Electricity by Country')
plt.xlabel('Percentage of Population with Access (%)')
plt.ylabel('Number of Countries')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(percent_access)  # Show all percentage values on x-axis
plt.show()
