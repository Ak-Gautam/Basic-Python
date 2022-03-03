# 3.	Write a Python program to define a function binary search to find a key element.

def binary_search(list, key):
    print(list)
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == key:
            return mid
        elif list[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# input list
lst = input("Enter a list of numbers separated by space: ").split()
lst = list(map(int, lst))
#lst.sort()
key = int(input("Enter a number to search: "))
res = binary_search(sorted(lst), key)
if res == -1:
    print("Number not found in the list")
else:
    print("Number found at index: ", res)