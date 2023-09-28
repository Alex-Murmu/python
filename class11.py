import pandas as pd

# Create a DataFrame with missing values
data = {'A': [1, 2, None, 4], 'B': [5, None, 7, 8]}
df = pd.DataFrame(data)

# Drop rows with missing values
df_cleaned = df.dropna()

# Fill missing values with a specific value
df_filled = df.fillna(0)
