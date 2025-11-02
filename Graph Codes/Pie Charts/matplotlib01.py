import matplotlib.pyplot as plt

# Data
movies = ['Comedy', 'Action', 'Romance', 'Drama', 'SciFi']
votes = [4, 5, 6, 1, 4]

# Plot
plt.pie(votes, labels=movies, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title('Favorite Type of Movie')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()
