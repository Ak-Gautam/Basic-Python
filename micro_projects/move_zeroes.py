# This one moves zeroes to the end of the array while maintaining the correct order of other elements
a = [0, 1, 12, 0, 17]

def move_ze(a):
    for i in range(len(a)):
        if a[i] == 0:
            temp = a[i]
            for j in range(i, len(a)-1):
                a[j] = a[j+1]
            a[len(a)-1] = temp
    return a
move_ze(a)
            
