# 13.	Write a program that generates a set of prime numbers and another set of odd numbers.

prime_set = set(i for i in range(2, 30) if all(i % j != 0 for j in range(2, i//2)))
odd_set = set(i for i in range(2, 30) if i % 2 != 0)

#Demonstrate the result of union, intersection, difference, and symmetric difference operations on these sets.
print("Prime set: ", prime_set)
print("Odd set", odd_set)

print("Union", prime_set.union(odd_set))
print("Intersection", prime_set.intersection(odd_set))
print("Difference", prime_set.difference(odd_set))
print("Symmetric difference", prime_set.symmetric_difference(odd_set))


