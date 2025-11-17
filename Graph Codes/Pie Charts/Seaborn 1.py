import seaborn as sns
import matplotlib.pyplot as plt

movies = ['Comedy', 'Action', 'Romance', 'Drama', 'SciFi']
votes = [4, 5, 6, 1, 4]
plt.pie(votes, labels=movies, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title('Favorite Type of Movie')
plt.axis('equal')
plt.show()
