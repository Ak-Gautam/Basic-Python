# Reverse only letters
# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"

def rev_letters(s):
    letters = [c for c in s if c.isalpha()]
    ans=[]
    for i in s:
        if i.isalpha():
            ans.append(letters.pop())            
        else:
            ans.append(i)
    return "".join(ans)

rev_letters(input("Enter the string\n"))
