import numpy as np
import sys

arr = np.array([1, 3, 4, 5, 6,], np.int8)
print(arr , arr.shape, arr.dtype )

arr3 = np.array([[1, 2, 3], [5, 0, 5], [39, 34, 50]])

print(arr3, arr3.dtype, arr3.shape, arr3.size)


print(np.zeros((2, 5)), "\n")  # all zero matrics

arr4 = np.arange(15)
print(arr4 , "\n")   # for numbers 0 to 14
print(np.linspace(1, 50, 5), "\n")  # for linearly spaced array

print(np.empty((4, 3)), "\n")  # for matrics with random entries

print(np.identity(6), "\n")  # for idnetity matrics of N * N
print(arr4.reshape(3, 5), "\n")  # to reshape a array in any other shape

print(arr4.ravel(), "\n")  # to get back in orignal shape

print(arr3.T, "\n")  # to get the transpose

print(arr3.sum(axis = 0))  # sum of all columns
print(arr3.sum(axis = 1), "\n")  # sum of all rows

print(arr3.ndim, arr3.nbytes)  # for no. of dimenssion and no. of bytes consumed in data storage

for item in arr3.flat:  # to get all the items
    print(item) 

print("\n" , arr3.argmax(), arr3.argmin(), "\n", arr3, "\n") #to get the index of max no. and min no.

print(arr3.argmax(axis = 0), arr3.argmax(axis = 1)) # to get max/min in row or column

print(arr3.argsort(axis = 1), "\n")


# for matrics operation ....

arr5 = np.array([[2, 3, 4], [56, 44, 23], [34, 56, 0]])

print(arr3 + arr5)
print( arr3 * arr5, "\n")  # element wise multiplication
print(np.sqrt(arr5), "\n")  # element wise sqrt

print(arr3.sum(), arr3.max(), arr3.min(), "\n") # to find ..  in whole matrics

print(arr3,"\n", np.where(arr3 <= 5), type(np.where(arr3 > 5))) # to get the position of respctive..

print(np.count_nonzero(arr3), "\n", np.nonzero(arr3), "\n")


# how efficient numpy array is

arr = [1, 2, 3, 5, 6]
np_arr = np.array(arr)
print(sys.getsizeof(1) * len(arr))
print(np_arr.itemsize * np_arr.size, "\n")

print(np_arr.tolist(), np_arr) #converts the np array back to python array