# numPy = numerical environment

import numpy as np 

mylist = [1,2,3]
print("mylist then numpy.array(mylist)")
print(mylist)
print(np.array(mylist), '\n')

nested_list = [[1,2],[3,4],[5,6]]

print("nested_list then numpy.array(nested_List)")
print(nested_list)
print(np.array(nested_list), "\n")

print("numpy.arrange() like range()")
print(np.arange(0,10))
print(np.arange(0,11,2), "\n")

#np.ones() does the same with ones
print("numpy.zeros() can take single number or shape(row, col):")
print(np.zeros(3))
print(np.zeros((4,6)), "\n")

#np linspace(0,10,3) start, stop, 3 numbers evenly spaced between them.
print(np.linspace(0,10,3))
print(np.linspace(0,10,21), "\n")

#np.eye() gives a matrix with diagonal of one
print(np.eye(5), "\n")

#np.random.rand(n) n random numbers between 0 and 1
#np.ranom.rand(row,col) gives matrix of random numbers btwn 0 and 1
print(np.random.rand(2))
print(np.random.rand(3,4), "\n")

#randn is similar but standard normal distribution
# centered around zero with a standard deposition of 1
# -1 to 1
print(np.random.randn(5,5), "\n")

#randint(start, stop, (row, col))
print(np.random.randint(1,100,(5,6)), "\n")

#seed call alawys to get same random numbers
np.random.seed(42)
print(np.random.rand(4), "\n")
#seed must always be run right before radom.rand


#reshape allows to reshape as matrix
#must reassign to keep. 
#use shape to get # elements. cannot reshape 25 into 2x3
arr = np.arange(25)
ranarr = np.random.randint(0,50,10)
print(arr.shape)
print(arr.reshape(5,5), '\n')

#max() gets max value, argmax() gets index of max value
# works same for min(), argmin()
print(ranarr.max())
print(ranarr.argmax(), "\n")

#dtype gets datatype
print(ranarr.dtype, "\n")

#index works similar to standard list
arr = np.arange(0,11)
print(arr[8])
print(arr[1:5])
print(arr[:5])
print(arr[5:])

#can re-set values in range
arr[3:6] = 100
print(arr)
# setting a variable to a slice of an array is actually just creating a pointer.
slice_arr = arr[3:6]
slice_arr[:] = 0
print(arr, "\n")
#have to copy()
arr_copy = arr.copy()
arr_copy[3:6] = 1
print(arr_copy)
print(arr, "\n")

arr_2d = np.array([[5,10,15], [20,25,30],[35,40,45]])
print(arr_2d)
print(arr_2d[0])
print(arr_2d[0][1])
print(arr_2d[0,1])
print(arr_2d[0:,1], "\n")

arr = np.arange(0,11)
print(arr>4)
bool_arr = arr>4
print(arr[bool_arr])
print(arr[arr>4])
print(arr-2)
print(arr+arr)
print(arr/arr)
print(1/arr, "\n")

print(arr.var())
print(arr.sum())
print(arr.std(), "\n")

arr2d = np.arange(0,25).reshape(5,5)
print(arr2d.shape)
print(arr2d)
print(arr2d.sum())
print(arr2d.sum(axis=0)) #axis=0 is sum of col
print(arr2d.sum(axis=1)) #sum of rows

