
'''

    Types of arguments:

    args: myfun(*args)

    kwargs: myfun(**kwargs)

'''

def add(*a):
    total=0

    for key,value in a.items():

        total+=value

    return total

print("Addition of all elements: ",add(12,35,46,70))
