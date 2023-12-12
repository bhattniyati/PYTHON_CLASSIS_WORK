
'''

    Lambda Function:
    
        -It is an anonymous function in python

        -It can take many arguments but can return single expression..

    Syntax of lambda function:

        Lambda Parameters: Expression

'''

x=int(input("Enter First Numb: "))
y=int(input("Enter Second Numb: "))
value= lambda x,y: x+y

print(value(x,y))
