#Taking the array input
a= []
n = int(input("Enter the lenth of the list\n"))
print("Enter the elements of the list\n")
for _ in range(n):
    a.append(int(input()))
    
#Sorting by parity (even, odd)
i, j = 0, 0
while j < n:
    if a[j] % 2 == 0 :
        a[i], a[j] = a[j], a[i]
        i += 1
    j += 1
print(a)
 
