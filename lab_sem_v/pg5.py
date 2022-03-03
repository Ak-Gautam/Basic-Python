# 5.	Write a program to print the 'n' Fibonacci series using recursion.

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


n = int(input("Enter the number of terms: "))
print("Fibonacci series: ")
for i in range(n):
    print(fib(i), end=" ")
