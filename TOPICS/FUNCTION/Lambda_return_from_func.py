

# Lambda function return from another function

x=int(input("Enter a number: "))

def add(x):

    return lambda y: x+y

n=(add(x))
print(n(30))
