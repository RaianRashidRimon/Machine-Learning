import seaborn as sns
import matplotlib.pyplot as plt

# Data
grades = ['A', 'B', 'C', 'D']
students = [4, 12, 10, 2]

# Plot
sns.barplot(x=grades, y=students, palette='Pastel1')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.title('Test Results')
plt.show()
