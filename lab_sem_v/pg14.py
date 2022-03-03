#Write a program that has a dictionary of names of students and a list of their marks in 4 subjects.
#Create another dictionary from this dictionary that has the name of the students and their total marks. Find out the topper and his/her score.
dict1 = {'A':[70,80,90,90],'B':[75,75,80,90]}
dict2 = {}
key = list(dict1.keys())
for i in key:
    dict2[i] = sum(dict1[i])
print(dict2)
topper = max(dict2.values())
for i in dict2.keys():
    if dict2[i] == topper:
        print(i, dict2[i])
        break