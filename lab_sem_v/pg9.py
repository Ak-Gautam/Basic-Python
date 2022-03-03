# 9.	Write a program to the following using reduce() function
# a.	Find largest number in a list
# b.	Find sum of the values in a list

list1 = [2, 5, 9, 1, 2, 4, 8, 5, 11, 2, 9]
from functools import reduce
print("Largest: ", reduce(lambda x, y: x if x > y else y, list1))
print("Sum:", reduce(lambda x, y: x + y, list1))
