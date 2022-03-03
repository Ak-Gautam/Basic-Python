# 17.	Using numpy :
# Create a 3x4 matrix filled with values from 10 to 21.

import numpy as np

mat = np.arange(10, 22).reshape(3, 4)
print(mat)

# create a 3x3 matrix filled with random values and print elements of 

mat1 = np.arange(11, 20).reshape(3, 3)
print("Mat:\n",mat1)
print("a\n", mat1[:2, 1:])
print("b\n", mat1[1:, 1:])
print("c\n", mat1[:, 1])
print("d\n", mat1[2, :])

#Create an element-wise comparison (greater, greater_equal, less and less_equal,equal, not_eqaul) of any two arrays each having a size of 2x2x3.

mat2 = np.arange(10, 22).reshape(2, 2, 3)
mat3 = np.arange(12, 24).reshape(2, 2, 3)
print("Matrices:\n", mat2,'\n', mat3)
print('\n',mat2 > mat3)
print(mat2 >= mat3)
print(mat2 < mat3)
print(mat2 <= mat3)
print(mat2 == mat3)
print(mat2 != mat3)

#Compute sum of all elements, sum of each column and sum of each row of a given array

element_sum = np.sum(mat2)
print("Sum of all elements: ", element_sum)
column_sum = np.sum(mat2, axis=0)
print("Sum of each column: ", column_sum)
row_sum = np.sum(mat2, axis=1)
print("Sum of each row: ", row_sum)