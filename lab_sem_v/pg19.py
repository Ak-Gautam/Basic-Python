# 19.	Using Pandas, perform the following:
# •	Convert a numpy array and dictionary to a Pandas series. 
# •	Convert Series of lists to one Series and sort the values.
# •	Find the positions of numbers that are multiples of 5 of a given integer number series.
# •	Number of occurrences of each unique value in a Series.
# •	Get the positions of items of a given series in another given series.

import pandas as pd
import numpy as np

np_ar = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

pd_ar = pd.Series(np_ar)
pd_dict = pd.Series(dict1)
print("Numpy Array: ", np_ar, "\nDictionary: ", dict1)
print("\nPandas Series: ", pd_ar, "\nPandas Dictionary: ", pd_dict)

s = pd.Series([[4, 5, 6], [1, 2, 3], [7, 8, 9]])
print("\nSeries of lists:\n", s)
# this below line will convert the series of lists to one series and sort the values
s = s.apply(pd.Series).stack().reset_index(level=1, drop=True)
s = s.sort_values()
print("\nSeries of lists after sorting the values:\n", s)

n_series = pd.Series(np.random.randint(1, 50, size=10))
print("Original series:", n_series)
a = n_series.to_numpy()
index = np.argwhere(a % 5 == 0)
print("Index of multiples of 5:", index)

item_count=  n_series.value_counts()
print("Unique value count:", item_count)

series1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
series2 = pd.Series([1, 3, 5, 7, 10])
# position of items of series2 in series1
result = [pd.Index(series1).get_loc(i) for i in series2]
print("Position of items of series2 in series1:", result)