# 11.	Write a python program to read a word and define a function that  check if a word contains three consecutive double letters or not.

def check_consecutive_double_letters(word):
    count = 0
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            count += 1
    return count

word = input("Enter a word: ")
if check_consecutive_double_letters(word) == 3:
    print("True")
else:
    print("False")