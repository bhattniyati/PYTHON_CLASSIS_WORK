

# Keyword Arguments:

# With kw_Arguments:


print("Using Keyword Arguments...")
def multi(**x):

    total=1

    for k,v in x.items():
        total*=v

    return total

print("Multiplication of all elements: ", multi(k1=3,k2=4,k3=5))

print()

# Without kw_Arguments:


print("Without Using Keyword Arguments...")
d1={"k1": 20, "k2": 30,"k3": 2}

def multi(x):

    total=1

    for k,v in x.items():
        
        total*=v

    return total

print("Multiplication of all elements: ",multi(d1))
