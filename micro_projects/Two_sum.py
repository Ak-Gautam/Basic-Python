# Two sum problem solution using brute force
def t_sum(a, k):
    sol = []
    flag = False
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] + a[j] == k:
                flag = True
                sol.append([a[i], a[j]])
    return flag, sol
k = int(input("Enter the sum \n"))
a = []
for _ in range(int(input("Enter the length of the array\n"))):
    a.append(int(input("Enter the array elements\n")))
print("In the array", a)
t_sum(a, k)
