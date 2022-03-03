# 8.	Write a python program that converts the list of temperatures in Celsius into Fahrenheit.

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
lst = [36.5,37,37.5,39]
print("Temp in celsius: ", *lst)
print("In farenheit: ", *list(map(celsius_to_fahrenheit, lst)))
