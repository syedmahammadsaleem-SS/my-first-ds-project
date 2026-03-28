# Data Cleaning Script
# Author: Syed Mahammad Saleem

import pandas as pd

# Sample dirty data
data = {
    'name': ['Alice', 'Bob', None, 'David'],
    'age': [25, None, 30, 22],
    'salary': [50000, 60000, 55000, None]
}

df = pd.DataFrame(data)

print("Before Cleaning:")
print(df)

# Clean the data
df = df.dropna()

print("\nAfter Cleaning:")
print(df)