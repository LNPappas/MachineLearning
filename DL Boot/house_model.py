import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('DL Boot/TF-Course-Notebooks/TF_Course_Notebooks/DATA/kc_house_data.csv')

# n = df.isnull().sum()
# print(n)

# print(df.describe().transpose())

plt.figure(figsize=(10,6))
# sns.distplot(df['price'])
# sns.countplot(df['bedrooms'])

print(df.corr()['price'].sort_values())

# sns.scatterplot(x='price', y='sqft_living', data=df)
sns.boxplot(x='bedrooms', y='price', data=df)


plt.show()