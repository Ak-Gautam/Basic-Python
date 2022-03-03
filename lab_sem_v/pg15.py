# 1.	Write a program to copy line by line from a file to another and count the number of words,
#  spaces, newline character, percentage of vowels and consonants in the file.

file_to_read="ReadData.txt"
file_to_write="WriteData.txt"

with open(file_to_read, 'r') as f:
    with open(file_to_write, 'w') as f1:
        for line in f:
            f1.write(line)

# count the number of words,
#  spaces, newline character, percentage of vowels and consonants in the file

with open(file_to_write, 'r') as f:
    count_words = 0
    count_spaces = 0
    count_newline = 0
    count_vowels = 0
    count_consonants = 0
    count_letters = 0
    for line in f:
        count_letters += len(line)
        count_words += len(line.split())
        count_spaces += line.count(' ')
        count_newline += line.count('\n')
        count_vowels += len([i for i in line if i in 'aeiouAEIOU'])
        count_consonants += len(list(c for c in line if c.isalpha() and c.lower() not in 'aeiou'))
    print("Number of words: ", count_words)
    print("Number of spaces: ", count_spaces)
    print("Number of newline: ", count_newline)
    print("Number of vowels: ", count_vowels)
    print("Number of consonants: ", count_consonants)
    print("Percentage of vowels: ", count_vowels/count_letters*100)
    print("Percentage of consonants: ", count_consonants/count_letters*100)