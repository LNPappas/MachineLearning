import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense

df = pd.read_csv('DL Boot/TF-Course-Notebooks/TF_Course_Notebooks/DATA/fake_reg.csv')

# print(df.head())
X = df[['feature1', 'feature2']].values
y = df['price'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = MinMaxScaler()
 #calculate what's needed from transformation to occur
scaler.fit(X_train)

#perform transformation
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# print(X_train.min(), X_train.max())

#create neural network layer
# model = Sequential([Dense(4, activation='relu'), 
#                     Dense(3, activation='relu'),
#                     Dense(1)])

#can also do this in seperate lines(prefered)
#can easily comment out a layer.
model = Sequential()
model.add(Dense(4, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1)) #final output layer (single numerical price value)

#atom optimizer with mean squared values loss
model.compile(optimizer='adam', loss='mse')

model.fit(x=X_train, y=y_train, epochs=250, verbose=0)

loss_df = pd.DataFrame(model.history.history)
# loss_df.plot()

#MSE
model.evaluate(X_test, y_test, verbose=0)

#loss
model.evaluate(X_train, y_train, verbose=0)

test_predictions = model.predict(X_test)
# print(test_predictions)

#prediction dataframes
test_predictions = pd.Series(test_predictions.reshape(300))
pred_df = pd.DataFrame(y_test)
pred_df = pd.concat([pred_df, test_predictions], axis=1)
pred_df.columns = ['Test True Y', 'Model Predictions']
print(pred_df)
sns.scatterplot(x='Test True Y', y='Model Predictions', data=pred_df)
plt.show()

mae = mean_absolute_error(pred_df['Test True Y'], pred_df['Model Predictions'])
mse = mean_squared_error(pred_df['Test True Y'], pred_df['Model Predictions'])
rmse = mean_squared_error(pred_df['Test True Y'], pred_df['Model Predictions'])**0.5
print('MAE:', mae, " MSE:", mse, ' RMSE:', rmse)
model.save('my_gem_model.h5')

new_gem = [[998, 1000]]
new_gem = scaler.transform(new_gem)
ng_p = model.predict(new_gem)
print(ng_p)