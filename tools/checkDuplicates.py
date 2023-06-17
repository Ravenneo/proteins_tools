import pandas as pd

# Replace 'your_csv_filename.csv' with the actual name of your CSV file
df = pd.read_csv('your_csv_filename.csv')
duplicates = df[df.duplicated()]
print(duplicates.head(10))
