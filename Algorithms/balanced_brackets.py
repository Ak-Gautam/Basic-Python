''' Given a sequence of brackets, how will you identify if its valid or not.
Example : ({[][]})

Output: Valid

Explanation: Every opening bracket has a closing bracket.

Example: ({[]]})

Output: Invalid

Explanation : Every opening bracket does not have a closing bracket.
'''

def bc(s):
    stack = []
    for i in s:
        if i in ['(', '[', '{']:
            stack.append(i)

        else:
            if not stack:
                return False
            cc = stack.pop()
            if cc == '(':
                if i != ')':
                    return False
            if cc == '{':
                if i != '}':
                    return False
            if cc == '[':
                if i != ']':
                    return False
    if stack:
        return False
    return True

    
s = input("Enter the sequence of the brackets in string form\n")
if bc(s):
    print("Valid\n")
else:
    print("Invalid\n")
        
