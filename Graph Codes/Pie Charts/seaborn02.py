import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set_style("whitegrid")

# Data
grades = ['A', 'B', 'C', 'D']
counts = [4, 12, 10, 2]

# Create pie chart with seaborn color palette
plt.figure(figsize=(8, 8))
plt.pie(counts, labels=grades, autopct='%1.1f%%', startangle=90,
        colors=sns.color_palette("pastel"))
plt.title('Grade Distribution in Recent Test')
plt.axis('equal')
plt.show()
