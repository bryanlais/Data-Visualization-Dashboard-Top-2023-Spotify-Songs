import pandas as pd
from io import StringIO

df = pd.read_csv("10x10.csv")
# Calculate averages for each released_month
averages = df.groupby('released_month').mean().reset_index()

# Create a new DataFrame with 12 rows for each month
result_df = pd.concat([averages] * 12, ignore_index=True)

# Save the result to a new CSV file
result_df.to_csv('area.csv', index=False)

print("New CSV file created: area.csv")