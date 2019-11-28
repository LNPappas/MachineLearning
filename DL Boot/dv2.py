import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('heart.csv')
# print(df.head())

plt.figure(figsize=(6,4))
# sns.distplot(df['age'], kde=False, bins=50, color='magenta')

# sns.countplot(x='cp', data=df, hue='sex', palatte='terrain')

# sns.boxplot(x='target', y='thalach', data=df, palette='prism',hue='sex')

sns.scatterplot(x='chol', y='trestbps', data=df, hue='sex', palette='Dark2', size='age')

# sns.pairplot(df, palette='prism')
plt.show()
