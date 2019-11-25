import numpy as np 

#Create an array of 10 zeros:
z = np.zeros(10)
print(z)

one = np.ones(10)
print(one)

five = np.ones(10)*5
print(five) 

arr = np.arange(10,51)
print(arr)

even = np.arange(10,51,2)
print(even)

matrix = np.arange(9).reshape(3,3)
print(matrix)

#3x3 identity matrix
print(np.eye(3))

r = np.random.rand()
print(r)

rlist = np.random.randn(25)
print(rlist)

mat = np.arange(0.01,1.01,.01).reshape(10,10)
print(mat)
#or:
mat = np.arange(1,101).reshape(10,10)/100 

l = np.linspace(0,1,20)
print(l)

mat = np.arange(1,26).reshape(5,5)
print(mat)
print(mat[2:, 1:])

print(mat[3,4])

print(mat[0:3,1:2])
print(mat[4])
print(mat[3:])
print(mat.sum())
print(mat.std())
print(mat.sum(axis=0))

#The seed value is a set random value that coorisponds with
# a number, so that random value can always be found.
# the number does matter as it coorisponds to the seed.

np.random.seed(42)
print(np.random.rand(4))

np.random.seed(52)
print(np.random.rand(4))

np.random.seed(42)
print(np.random.rand(4))