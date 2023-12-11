
# Task 2: Choice Board

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def multi(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

def modulo(num1,num2):
    return num1%num2


def menu():

    print("\n==========Choice Board==========\n")
    print("\n\t1.Addition")
    print("\t2.Substraction")
    print("\t3.Multiplication")
    print("\t4.Division")
    print("\t5.Modulo")
    print("\t6.Exit")

status=True
while status:
    
    menu()
    choice= int(input("\n\tEnter Your Choice: "))
        
    if choice==1:
        num1=int(input("\n\tEnter First Number: "))
        num2=int(input("\tEnter Second Number: "))
        print("\n\tYour Ans:",add(num1,num2))

    elif choice==2:
        num1=int(input("\n\tEnter First Number: "))
        num2=int(input("\tEnter Second Number: "))
        print("\n\tYour Ans:",sub(num1,num2))

    elif choice==3:
        num1=int(input("\n\tEnter First Number: "))
        num2=int(input("\tEnter Second Number: "))
        print("\n\tYour Ans:",multi(num1,num2))

    elif choice==4:
        num1=int(input("\n\tEnter First Number: "))
        num2=int(input("\tEnter Second Number: "))
        print("\n\tYour Ans:",div(num1,num2))

    elif choice==5:
        num1=int(input("\n\tEnter First Number: "))
        num2=int(input("\tEnter Second Number: "))
        print("\n\tYour Ans:",modulo(num1,num2))

    elif choice==6:
        print("\n\tExit")
        break
    
    else:
        print("\n\tInvalid Choice..Please Enter a number between 1 and 6.")
        break
        
    ch= input("\n\tDo You Want To Continue? ['y/n']: ")

    if ch=='y' or ch=='Y':
        print("\n\tRepeat The Process..")
        status=True

    else:
        print("\n\tThank You !!")
        status=False
