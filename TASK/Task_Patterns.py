
print("Pattern:1")
for x in range(1,6):
    for i in range(1,x+1):
        print("*",end=" ")
    print()

print()



print("Pattern:2")
for x in range(1,6):
    for i in range(1,x+1):
        if i % 2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()

print()



print("Pattern:3")
num=1
for x in range(1,5):
    for i in range(1,x+1):
        print(num,end=" ")
        num= num+1
    print()

print()


print("Pattern:4")
a=65
for x in range(1,6):
    for i in range(1,x+1):
        print(chr(a),end=" ")
        a= a+1
    print()

print()

print("Pattern:5")
for x in range(1,6):
    a=65
    for i in range(1,x+1):
        print(chr(a),end=" ")
        a= a+1
    print()

print()


print("Pattern:6")
for x in range(1,6):
    print(' '*(6-x)+"*"*x)

print()



print("Pattern:7")
for x in range(5,0,-1):
    for i in range(0,x):
        print("*",end=" ")
    print()

print()



print("Pattern:8")
for x in range(1,6):
    print(' '*(6-x)+" *"*x)

print()



print("Pattern:9")
for x in range(6,1,-1):
    print(' '*(6-x)+" *"*x)

print()


print("Pattern:10")
for x in range(5):
    for i in range(5):
        if x==i:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()




