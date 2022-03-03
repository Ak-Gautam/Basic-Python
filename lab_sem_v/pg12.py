# 12.	Write a program to sort a given list, in the sorted list the value of the first element should be maximum, the second value should be the minimum,
# the third should be the second maximum, the forth should be the second minimum and so on.

def sort_list(lst):
    lst.sort()
    print("Sorted list: ", lst)
    ic = 0
    while ic < len(lst):
        lst.insert(ic, lst.pop())
        ic += 2
    return lst


list1 = [2, 5, 9, 1, 2, 4, 8, 5, 11, 2, 9]
print(sort_list(list1))