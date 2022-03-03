# 6.	Write a python program to demonstrate the following.
# a.	Find list1[2:5],list1[::2],list1[1::3] for the given list list1= [1,‘a’,”Hello”, [2,3,4,5,6], 4.5]
list1 = [1, 'a', "Hello", [2, 3, 4, 5, 6], 4.5]
print(list1[2:5], list1[::2], list1[1::3])
# b.	Append new values in the list
list1.append(7)
print(list1)
# c.	Remove existing values in the list
list1.remove(7)
print(list1)
# d.	 Insert a list in another list	
list1.insert(0, [1, 2, 3])
print(list1)
# e.	Check if a element is present or not in a list
print('a' in list1)
# f.	Concatenate two lists
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
# g.	Insert a element at a specified index in the list
list1.insert(2, "Hello")
# h.	Reverse the elements in the list
list1.reverse()
print(list1)
# i.	Print list of cubes using list comprehensive 
print(*[i**3 for i in range(6)])

