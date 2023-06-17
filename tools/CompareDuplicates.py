import pandas as pd

# Load the two CSV files
df_set = pd.read_csv('test1.csv')
df_list = pd.read_csv('test2.csv')

# Check if the two DataFrames are identical
print(df_set.equals(df_list))  # This will print 'True' if the DataFrames are identical

# Find the number of unique entries in the list-based DataFrame
num_unique_in_list = df_list['ID'].nunique()
print(f"Number of unique entries in the list-based DataFrame: {num_unique_in_list}")

# Compare this with the length of the set-based DataFrame
num_in_set = len(df_set)
print(f"Number of entries in the set-based DataFrame: {num_in_set}")

# If the numbers are the same, the discrepancy was due to duplicates. If they're different, there's another issue.
if num_unique_in_list == num_in_set:
    print("The discrepancy was due to duplicate entries.")
else:
    print("There's another issue causing the discrepancy.")
