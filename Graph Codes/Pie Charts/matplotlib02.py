import matplotlib.pyplot as plt

# Data
grades = ['A', 'B', 'C', 'D']
counts = [4, 12, 10, 2]

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(counts, labels=grades, autopct='%1.1f%%', startangle=90)
plt.title('Grade Distribution in Recent Test')
plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle
plt.show()
