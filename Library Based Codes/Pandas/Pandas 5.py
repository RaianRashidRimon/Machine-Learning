import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

# Write DataFrame to a CSV file
df.to_csv('people.csv', index=False)

print("Data written to 'people.csv'.")
