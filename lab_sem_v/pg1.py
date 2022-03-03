# 1.	Write a python program to perform the following.

# a.	Find length of a string( not using len() function).

str1 = input("Enter a string: ")
count = 0
for i in str1:
    count += 1
print("Length of the string is: ", count)

# b.	Count the number of occurrences of a specific character  in a string.
ch = input("Enter a character: ")
print("Number of occurrences of "+ch+" in the string is: ", str1.lower().count(ch))