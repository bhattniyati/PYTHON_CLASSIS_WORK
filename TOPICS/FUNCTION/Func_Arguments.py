
'''

    Types of arguments:

    args: myfun(*args)

    kwargs: myfun(**kwargs)

'''

# Arguments:

print("Using Arguments...")

def add(*a):
    total=0

    for i in a:
        total+=i

    return total

print("Addition of all elements: ",add(12,35,46,70))

print()

print("Without Using Arguments...")

s1=[3,4,5,6]

def multi(a):
    total=1

    for i in a:
        total*=i

    return total

print("Substraction of all elements: ",multi(s1))
print(s1)



    
