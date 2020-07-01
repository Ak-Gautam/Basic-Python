''' 
Find the missing no. inn a given array
'''

a = []
sol = 'NaN'
for _ in range(int(input("Enter the length of the array\n"))):
    a.append(int(input("Enter the array elements\n")))
    
for i in range(min(a), len(a)):
    if i not in a:
        sol = i
if sol != 'NaN':
    print("Missing number is ", sol)
else:
    print("Completed array")
