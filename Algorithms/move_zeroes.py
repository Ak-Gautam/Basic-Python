# This one moves zeroes to the end of the array while maintaining the correct order of other elements
def move_ze(a):
    for i in range(len(a)):
        if a[i] == 0:
            temp = a[i]
            for j in range(i, len(a)-1):
                a[j] = a[j+1]
            a[len(a)-1] = temp
    return a

#Moving zeroes without using extra variable. 
def move_zer(a):
    indx = 0
    for i in range(len(a)):
        if a[i] != 0:
            a[indx] = a[i]
            indx += 1
    for j in range(indx , len(a)):
        a[j] = 0
    return a
#Taking user input for the array
a = []
for _ in range(int(input("Enter the length of the array\n"))):
    a.append(int(input("Enter the array elements\n")))
move_zer(a)
move_ze(a)            
            
