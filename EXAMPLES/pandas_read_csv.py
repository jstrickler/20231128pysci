import pandas as pd

df = pd.read_csv('../DATA/sales_records.csv', parse_dates=["Order Date", "Ship Date"])  # Read CSV data into dataframe. Pandas automatically uses the first row as column names

print(df.describe())  # Get statistics on the numeric columns (use `df.describe(include='O')` for text columns)
print()

print(df.info())  # Get information on all the columns ('object' means text/string)
print()

print(df.head(5))  # Display first 5 rows of the dataframe (`df.describe(__n__)` displays n rows)

df['total_sales'] = df['Units Sold'] * df['Unit Price']
pd.options.display.width = 1000
pd.options.display.max_columns = 100
print(df)

print(df.info())
print(df.describe(include='O'))

