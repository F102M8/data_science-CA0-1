import pandas as pd

df = pd.read_csv("data.csv", index_col=0)
print(df.head())

cleansed_df = pd.DataFrame()

columns_to_be_deleted = list(filter(lambda x: x not in ['Txn Fee', 'Value'], df.columns))

print(f"1. deleting these columns: {columns_to_be_deleted}")
df.drop(columns_to_be_deleted, axis=1, inplace=True)

print(f"2. filtering data by whether their Value ends with 'ETH'")
df = df[df['Value'].str.endswith('ETH')]

print(f"3. turning Txn Fee column into float")
df['Txn Fee'] = pd.to_numeric(df['Txn Fee'], errors='coerce')

print(f"4. turning Value column into float")
df['Value'] = df['Value'].str.replace(' ETH', '').astype(float)

print(f"5. dropping duplicates")
df.drop_duplicates(inplace=True)

print(f"6. dropping nan cells")
df.dropna(subset=['Txn Fee', 'Value'], inplace=True)

print(f"saving data in 'cleansed_data.csv'")
df.to_csv('cleansed_data.csv')
