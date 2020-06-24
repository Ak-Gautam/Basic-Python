#This program takes a list of words and a list of letters as input and find the words that can be formed using the letters .
#A character can't appear twice consecutively but can appear twice in the same word. i.e. Ball: wrong  Bomb:correct

def charCount(i):  #this function counts the number of times the char has appeared and creates a dictionary based on it.
    dict = {} 
    for j in i: 
        dict[i] = dict.get(j, 0) + 1
    return dict

def possible_words(words, charSet):  #This function checks is the word is possible
    for i in words: 
        flag = 1
        chars = charCount(i) 
        for key in chars: 
            if key not in charSet: 
                flag = 0
        else: 
            if charSet.count(key) != chars[key]: 
                flag = 0
        if flag == 1: 
            print(i)
            
input = ['go', 'bat', 'me', 'eat', 'toss', 'craft', 'lift', 'goal', 'dog', 'boy', 'run', 'bomb', 'ball', 'tell'] 
charSet = ['e', 'o', 'b', 'a', 'm', 'g', 'l'] 
possible_words(input, charSet) 
 
