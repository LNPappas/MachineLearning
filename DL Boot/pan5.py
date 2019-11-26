import pandas as pd

df = pd.read_csv(r'C:\Users\wooho\OneDrive\Documents\GitHub\ML_DS\DL Boot\Universities.csv')
df.columns = ['1', '2', '3', '4', '5']

df.to_csv('output.csv', index=False)

dt = pd.read_csv('output.csv')
print(dt)