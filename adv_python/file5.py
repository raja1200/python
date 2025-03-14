import pandas as pd
df = pd.read_csv('data.csv')

df.loc[7, 'Duration'] = 45

print(df.to_string())

print(df.duplicated().to_string())
df.drop_duplicates(inplace = True)

print(df.to_string())
print(df.corr()) #relation between columns : range -1 to 1