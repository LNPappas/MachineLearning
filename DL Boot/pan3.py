#GroupBy

import pandas as pd 

df = pd.read_csv(r'C:\Users\wooho\OneDrive\Documents\GitHub\ML_DS\DL Boot\Universities.csv')
print(df.head(), '\n')
print(df.groupby('Year').sum().sort_index(ascending=False), '\n')
print(df.groupby('Year').mean(), '\n')
print(df.groupby(['Year', 'Sector']).sum(), '\n')
print(df.groupby('Year').describe(), '\n')
print(df.groupby('Year').describe().transpose(), '\n')