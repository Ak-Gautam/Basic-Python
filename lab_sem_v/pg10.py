# 10.	Write a program to separate an even and odd numbers in a given tuple.

tup=(2,3,4,5,6,7,8)
even = tuple(i for i in tup if i%2==0)
odd = tuple(i for i in tup if i%2!=0)
print("Even: ", even,"\nOdd: ", odd)