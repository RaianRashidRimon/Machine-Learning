import seaborn as sns
import matplotlib.pyplot as plt

percent_access = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
countries = [5, 6, 12, 5, 4, 5, 6, 10, 15, 34]





plt.figure(figsize=(10, 6))
sns.scatterplot(x=percent_access, y=countries, size=100, sizes=(100, 100), alpha=0.6)
plt.title('Access to Electricity by Country')
plt.xlabel('Percentage of Population with Access (%)')
plt.ylabel('Number of Countries')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(percent_access)
plt.show()
