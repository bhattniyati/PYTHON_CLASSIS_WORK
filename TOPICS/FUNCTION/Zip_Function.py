
'''

    Zip(): Zip function

'''


l1=[12,3,4,50,67]
l2=[20,40,45,7]
l3=[20,4,5,6,7,8,9]

zip1=(zip(l1,l2,l3))

# *: Unpack Operator

a,b,c=zip(*zip1)

print(a)
print(b)
print(c)
