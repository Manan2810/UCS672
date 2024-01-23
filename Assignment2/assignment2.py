import numpy as np
from numpy import random
#Q1 
array_of_five = np.full(10,5)
print(array_of_five)

#Q2
array_integers = np.arange(10,51)
print(array_integers)

#Q3
array_integers = np.arange(10,51,2)
print(array_integers)

#Q4
matrix_1 = np.arange(9)
matrix_3x3 = matrix_1.reshape(3,3)
print(matrix_3x3)

#Q5
x = random.normal(size=(25))
print(x)

#Q6
array_2 = np.arange(0,1.01,0.01)
print(array_2)

#Q7
linear_array = np.linspace(0, 1, 20)
print(linear_array)

#Q8
matrix_5x5 = (np.arange(1,26)).reshape(5,5)
print(matrix_5x5)

print(matrix_5x5[2:5,1:5])
print(np.array(matrix_5x5[0:3,1]))

mat = matrix_5x5.sum()
print(mat)

row_sums = np.sum(matrix_5x5, axis=1)
col_sums = np.sum(matrix_5x5, axis=0)
print(row_sums,",",col_sums)
