import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

x = [0,1,2]
y = [100,200,300]

# plt.plot(x,y)

housing = pd.DataFrame({'rooms':[1,1,2,2,2,3,3,3], 'price':[100,120,190,200,230,310,330,305]})

plt.scatter(housing['rooms'], housing['price'], color='#bc67c9', marker='*')
plt.title('Housing Scatter Plot')
plt.xlabel('Rooms', color='blue')
plt.ylabel('Price', color='red')
plt.xlim(0,3)
plt.ylim(0,300)
plt.show()

