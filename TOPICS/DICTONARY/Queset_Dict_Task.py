queset = {
    'Q1': {'Q': "Sun rise from?", 'A': "East"},
    'Q2': {'Q': "How is a code block indicated in Python?", 'A': "Indetation"},
    'Q3': {'Q': "What will be the datatype of the var: var=10? ", 'A': "Int"},
    'Q4': {'Q': "What will be the datatype of the var: var=Hello? ", 'A': "Str"},
    'Q5': {'Q': "Which type of loops are not supported in python?", 'A': "do-while"}
    }


for k,v in queset.items():

    question= v['Q']

    Ans= input(f"{k}: {question} ")

    print("Ans: ", Ans)
