#A program to print the fibonacci series upto a given length
n = int(input("Input the limit\n"))
print("The first", n, "fibonacci series is \n")
f1 = 0
f2 = 1
if n == 1:
    print(f1)
elif n > 1:
    print(f1, f2, end = " ")
    for _ in range(1, n-1):
        f3 = f1 + f2
        print(f3, end = " ")
        f1 = f2
        f2 = f3
