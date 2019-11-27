import pandas as pd

df = pd.read_csv(r'C:\Users\wooho\OneDrive\Documents\GitHub\ML_DS\DL Boot\Universities.csv')
df.columns = ['1', '2', '3', '4', '5']

df.to_csv('output.csv', index=False)
dt = pd.read_csv('output.csv')

bank = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')

soccer = pd.read_html('https://fbref.com/en/comps/182/NWSL-Stats.html')
print(soccer)