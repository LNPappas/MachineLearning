import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv('DL Boot/TF-Course-Notebooks/TF_Course_Notebooks/DATA/diamonds.csv')
# print(df.head())

plt.figure(figsize=(6,4))
# sns.scatterplot(y='price', x='carat', data=df, alpha=0.1, edgecolor=None)

# sns.distplot(df['price'], kde=False)
# plt.xlim=(0,18000)
# plt.ylim=(0,9500)

# sns.countplot(data=df, x='cut')

sns.boxplot(data=df, x='cut', y='price', order=['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'], palette='cool')
plt.show()