# Basic data_structures in python


#List
list1 = [1, 2, 3, 'e', "Gautam"]
print(list1)
list1.append(2)
print(list1)
list1.append((2,0))
print(list1)
list1.extend((2,0))
print(list1)


a = list1.pop(3)
print(a)
print(list1)
list1.remove(2)
print(list1)
del list1[1]
print(list1)
print(list1.index("Gautam"))


list2 = [0, 0.5, 2, 3, 'a', "Gautam", 9, 7]
print(list2)
print("After the required opertions.\n")
#print(list2[from:to])
print(list2[1:5])
print(list2[::-1])
print(list2[0:7:2])



list3 = [2, 6, 4, 82, 21, 786]
print(list3)
#list3 = sorted(list3)
print(sorted(list3))
list3.sort(reverse=True)
print(list3)



#Tuple
tuple1 = (2, 3, 4, 5, 6, 7)
print(tuple1)
tuple1 += (8, 9, 10)
print(tuple1)
#Can add but can't substract




#Dictionary
dict1 = {1: 'Python', 2: 'JS', 3: 'C'}
print(dict1)
dict1[4] = 'Java'
print(dict1)
print(dict1[3])
print(dict1.pop(2))
print(dict1)
del dict1[1]
print(dict1)
print(dict1.items())
print(dict1.values())
print(dict1.keys())


#Sets
set1 = {1, 2, 3, 3, 4, 4, 4, 6}
print(set1)
set1.add(8)
print(set1)
set2 = {4, 6, 10, 11, 12, 13}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
