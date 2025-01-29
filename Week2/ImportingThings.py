import array as ar
import numpy as np

a1 = np.array([1,2,3,10])
a2 = np.zeros(10)
a3 = np.zeros(10, dtype = int)
a4 = np.arange(0,10)
a5 = np.random.randint(1,100,5)
a6 = np.empty(3)
a7 = np.ones((3,5))
a8 = np.ones((3,5), dtype = int)
a9 = np.full((3,5),12)
a10 = np.random.randint(1,100,(3,5))

# some np.methods: .min .max .mean .median .sum .prod

# numpy arrays can be sliced, can be indexed into from -1, concatenated
# all values must be of the same type
# 3 dimensional array can be indexed into using the index of the row, then of the column

print(a1 + 5) 
print(a1 - 5)
print(a1 * 5)
print(a1 % 5)
print(a1 ** 5)
print(a1 // 5) 

print(a1 < 3) # returns an array of bools 
print((a1 * 2) == (a1 ** 2)) # also returs an array of bools, with the *2 and **2 done to each side respectively

# these only work if the arrays have the same length

print(a10)
print(len(a10))