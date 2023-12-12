'''

queset = {
    'Q1': {'Q': "Sun rise from?", 'A': "East"},
    'Q2': {'Q': "How is a code block indicated in Python?", 'A': "Indetation"},
    'Q3': {'Q': "What will be the datatype of the var: var=10? ", 'A': "Int"},
    'Q4': {'Q': "What will be the datatype of the var: var=Hello? ", 'A': "Str"},
    'Q5': {'Q': "Which type of loops are not supported in python?", 'A': "do-while"}
    }

'''


queset= {}

for i in range(1,11):

    User_Que= input(f"Enter A Que{i}? ")
    User_Ans= input(f"Enter Ans: ")

    key= f'Q{i}'     #store in key

    queset[key]={'Q':User_Que,'A': User_Ans}

print(queset)


