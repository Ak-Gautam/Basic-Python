# 20.	Using Pandas, perform the following:
# •	Create and display a dataFrame from a dictionary of names of the student, subjects, grade of respective subject, number of each attempt and qualify data which has the index labels.
# •	Display the details of a specified student.
# •	Select the rows where the number of attempts in the examination is greater than 2 and score less than 40.
# •	Select the rows where the number of attempts in the examination is less than 2 and score greater than 15.
# •	Sort the data frame first by 'name' in descending order, then by 'score' in ascending order.

import pandas as pd

exam_data  = {'name': ['Anil', 'Avinash', 'Kaveri', 'James', 'kavitha'],
                         'Subjects': ["Kannada", "English", "Hindi", "Tamil", "Telagu"],
                         'attempts': [1, 3, 2, 3, 2],
                         'qualify': ['yes', 'no', 'yes', 'no', 'no'],
                        'Score':[30,12,32,14,40]}
labels = ['a', 'b', 'c', 'd', 'e']

df = pd.DataFrame(exam_data , index=labels)
print(df)

df = pd.DataFrame(exam_data , index=labels)
print(df.iloc[:1])

print("Number of attempts in the examination is greater than 2 and score less than 40 :")
print(df[(df['attempts'] > 2) & (df['Score'] < 40)])

print("Number of attempts in the examination is less than 2 and score greater than 15 :")
print(df[(df['attempts'] < 2) & (df['Score'] > 15)])

print("'name' in descending order")
print(df.sort_values(by=['name','Score'],ascending=[True,False]))
print("'Score' in ascending order")
print(df.sort_values(by=['name','Score'],ascending=[False,True]))


