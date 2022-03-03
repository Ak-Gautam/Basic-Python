# 2.	Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
#  Return the n copies of the whole string if the length is less than 2.

n = int(input("Enter the number of copies: "))
str1 = input("Enter a string: ")
if len(str1) < 2:
    print((str1+" ") * n)
else:
    print((str1[:2]+" ") * n)