import matplotlib.pyplot as plt

grades = ['A', 'B', 'C', 'D']
counts = [4, 12, 10, 2]
plt.figure(figsize=(8, 8))
plt.pie(counts, labels=grades, autopct='%1.1f%%', startangle=90)
plt.title('Grade Distribution in Recent Test')
plt.axis('equal')  
plt.show()
