import seaborn as sns
import matplotlib.pyplot as plt
fruits = ['Apple', 'Orange', 'Banana', 'Kiwifruit', 'Blueberry', 'Grapes']
people = [35, 30, 10, 25, 40, 5]
sns.barplot(x=fruits, y=people, palette='Blues_d')
plt.xlabel('Fruit')
plt.ylabel('Number of People')
plt.title('Survey Results: Nicest Fruit')
plt.show()
