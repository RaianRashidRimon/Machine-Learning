import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'New York': [0, 2, 8, 14, 20, 25, 28, 27, 29, 16, 17],
    'Chicago': [-3, 0, 5, 12, 18, 23, 26, 25, 21, 14, 7],
    'Los Angeles': [14, 15, 16, 17, 19, 21, 23, 24, 23, 21, 18],
    'Miami': [21, 23, 23, 24, 26, 28, 29, 28, 26, 24, 22]
}
df = pd.DataFrame(data, index=[f'Day {i+1}' for i in range(11)]).T
plt.figure(figsize=(10, 6))
sns.heatmap(
    df, 
    annot=True,  # show temperature values in cells
    cmap='YlOrRd',  # color scheme: Yellow to Red
    fmt='d', # integer format for annotations
    linewidths=0.5, # grid line width
    cbar_kws={'label': 'Temperature (°F)'},  # Colorbar label
    square=False # non-square cells for better readability
)
plt.title('Temperature Heatmap Across Cities and Days', fontsize=14)
plt.xlabel('Days')
plt.ylabel('Cities')
plt.show()
