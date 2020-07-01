'''
Find the local maxima in the given array (even more than one)
'''

a = []
sol = []
for _ in range(int(input("Enter the length of the array\n"))):
    a.append(int(input("Enter the array elements\n")))
    
if a[0] > a[1]:
    sol.append(a[0])
if a[len(a)-1] > a[len(a)-2]:
    sol.append(a[len(a)-1])
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        sol.append(a[i])
for i in range(0, len(sol), 2):
    print(sol[i], sol[i+1], sep = ' or ')
