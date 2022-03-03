# 2.	Write a program to create a text file “MyFile.txt” and write a few lines into it. 

n = int(input("Enter the number of lines: "))
file_to_write="MyFile.txt"
with open(file_to_write, 'a') as f:
    for i in range(n):
        line = input("Enter the line: ")
        f.writelines(line)
        f.write('\n')

# Replace all the spaces from text with - (dash).
with open(file_to_write, 'r') as f:
    for line in f:
        line = line.replace(' ', '-')
