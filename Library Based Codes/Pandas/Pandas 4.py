import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

# Filter data where Age is greater than 30
filtered_df = df[df['Age'] > 30]

# Display the filtered DataFrame
print("Filtered DataFrame:")
print(filtered_df)
