import numpy as np 
import pandas as pd 
from numpy.random import randint

#Dataframes
column = ['W','X','Y','Z']
index = ['A','B','C','D','E']

np.random.seed(42)
data = randint(-100, 100,(5,4))

#Dataframes columns
df = pd.DataFrame(data, index, column)
print(df)
print(df[['W']])
print(df[['Z','W']])

df['N'] = df['W']+df['Y']
print(df, '\n')

df = df.drop('N', axis=1)
print(df, '\n')

#DataFrames rows:
print(df.loc['A'])
print(df.loc[['A', 'E']])

print(df.iloc[1:3])

print(df.loc['A', 'W'])

print(df > 0)
print(df[df>0])
print(df['X']>0)
print(df[df['X']>0])
print(df[(df['W']>0)&(df['Y']>1)])

new_ind = ['CA','NY','WY','OR','CO']
df['States'] = new_ind
df = df.set_index('States')
print(df, '\n')
print(df.describe(), '\n')
print(df.info(), '\n')