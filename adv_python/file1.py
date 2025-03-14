import pandas as pd

df = pd.read_csv('data.csv')
print(df.to_string())
print(df.head())
print(df.tail())
print(df.sample(10))
print(df.info())
print(df.describe()) #to gat statistical information
print(df.isnull().sum()) #infromation about Null
print(df.duplicated().to_string())
print(df.duplicated().sum())
new_df = df.dropna()  #to remove rows conatins NULL
print(new_df.to_string())