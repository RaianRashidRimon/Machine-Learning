import matplotlib.pyplot as plt

# Data
grades = ['A', 'B', 'C', 'D']
students = [4, 12, 10, 2]

# Plot
plt.bar(grades, students, color='lightgreen')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.title('Test Results')
plt.show()
