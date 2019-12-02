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

# print(df.corr()['price'].sort_values())

# sns.scatterplot(x='price', y='sqft_living', data=df)
# sns.boxplot(x='bedrooms', y='price', data=df)

# sns.scatterplot(x='price', y='long', data=df)
# sns.scatterplot(x='price', y='lat', data=df)

# sns.scatterplot(x='long', y='lat', data=df, hue='price')

# p = df.sort_values('price', ascending=False).head(20)
# print(p)
# print(len(df))
top =int((len(df)*0.01)//1)
bottom_percent = df.sort_values('price', ascending=False).iloc[top:]

# sns.scatterplot(x='long', y='lat', data=bottom_percent, hue='price', edgecolor=None, alpha=0.2, palette='RdYlGn')

# sns.boxplot(x='waterfront', y='price', data=df)

df = df.drop('id', axis=1)
df['date']=pd.to_datetime(df['date'])
df['year'] = df['date'].apply(lambda date: date.year)
df['month'] = df['date'].apply(lambda date: date.month)
df = df.drop('date', axis=1)
# df.groupby('month').mean()['price'].plot()
# df.groupby('year').mean()['price'].plot()

# print(df.columns)

#drop zipcode for this course
# zipcode could actually be very useful, but requires time to group and 
# evaluate areas. Too much for this problem.

df = df.drop('zipcode', axis=1)

# print(df['yr_renovated'].value_counts())
#higher year house renovated == more value

# print(df['sqft_basement'].value_counts())
X = df.drop('price', axis=1).values
y = df['price'].values

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=101)

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# print(X_train.shape)

model = Sequential()
model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mse')
model.fit(x=X_train, y=y_train, 
            validation_data=(X_test, y_test), 
            batch_size=128, epochs=400)

losses = pd.DataFrame(model.history.history)
# losses.plot()

from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)

rmse = np.sqrt(mean_squared_error(y_test, predictions))
mae = mean_absoulte_error(y_test, predictions)
evs = explained_varience_score(y_test, predictions)

# df['price'].describe()

# plt.scatter(y_test, predictions)

single_house = df.drop('price', axis=1).iloc[0]
single_house = scaler.transform(single_house.values.reshape(-1,19))
model.predict(single_house)
print(df.head(1))


# plt.show()