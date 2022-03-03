# 18.	Using numpy, perform the following:
# ●	Compute the x and y coordinates for points on a sine curve and plots the points using matplotlib.
# ●	Create a 3x4 matrix and find any missing data, number of zeros in a given array.
# ●	Create a matrix of randomly generated data of shape (4, 4) and replace all positive values with 2 and all negative values with –2. 
# ●	Swap the rows and columns of a given array in reverse order.
# ●	Find common values between two arrays.

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5 * np.pi, 0.2)
y = np.sin(x)
print("Plot the points using matplotlib:")
plt.plot(x, y)
plt.show()

nums = np.array([[3, 0, np.nan, 1], [10, 12, 0, 9],[5, np.nan, 1, np.nan]])
print("Original array:") 
print(nums)
print("\nMissing data of the said array:")
print(np.isnan(nums))
print("\nNumber of zeros in a given array:",nums.size-np.count_nonzero(nums))
print("\nHere: - :",sum(sum(nums==0)))

arr = np.random.randn(4, 4)
print(arr)
np.where(arr > 0, 2, -2)

nums = np.array([[[1, 2, 3, 4], [0, 1, 3, 4], [90, 91, 93, 94], [5, 0, 3, 2]]])
print("Original array:")
print(nums)
print("\nSwap rows and columns in reverse order:")
new_nums = print(nums[::-1, ::-1])

randnums1= np.random.randint(1,100, size=(3,3))
print("array 1:",randnums1)
randnums2= np.random.randint(1,100, size=(3,3))
print("array 2:",randnums2)
print("Common elements are:")
print(np.intersect1d(randnums1, randnums2))

