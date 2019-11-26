# pandal data built off numpy
import numpy as np 
import pandas as pd 

#panda series
labels = ['a','b','c']
mylist = [10,20,30]
arr = np.array(mylist)
d = {'a':10, 'b':20, 'c':30}
p = pd.Series(data=mylist)
print(p, '\n')
p = pd.Series(data=mylist, index=labels)
print(p, '\n')
p1 = pd.Series(arr, labels)
print(p1, '\n')
print(pd.Series(d))
sales1 = pd.Series([250,450,200,150],['USA', 'CHINA', 'INDIA', 'BRAZIL'])
sales2 = pd.Series([260,500,210,100],['USA', 'CHINA', 'INDIA', 'JAPAN'])
print(sales1, '\n', sales2, '\n')
print(sales2[3], sales2['JAPAN'], '\n')
print(sales1 + sales2)


