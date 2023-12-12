

'''
    Map(): Map Function
    
'''


def sqrt(y):
    return y*y*y

t1=(3,4,5,6,7)
print(tuple(map(sqrt,t1)))

print()

def sqrt(y):
    return y*y*y

l1=[3,4,5,6,7]
print(list(map(sqrt,l1)))

print()

def add(y):
    return y+y

l1=[3,4,5,6,7]
print(list(map(add,l1)))

print()

def add_val(x,y):
    return x+x,y+y

d1=[3,4,5,6,7]
d2=[5,6,7,8,9]
print(list(map(add_val,d1,d2)))




