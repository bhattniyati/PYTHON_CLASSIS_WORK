'''

luckynum=40


status=True
while status:
    num=int(input("Guess The Number: "))
    if num>luckynum:
        print("Hint: Think Lesser Number..")
     
    elif num<luckynum:
        print("Hint: Think Larger Number..")
    
    elif num==luckynum:
        print("Guess Right Answer..")
        break

'''

luckynum=40

status=True

while status:
    for num in range(1,6):
        
        num=int(input("Guess The Number: "))
    
        if num>luckynum:
            print("Hint: Think Lesser Number...")

        elif num<luckynum:
            print("Hint: Think Larger Number...")

        elif num==luckynum:
            print("Guess Right Answer...")
            break
            

    ch= input("Do You Want To Again? ['y/n']: ")
    if ch=='Y' or ch=='y':
        status=True
           
    else:
        status=False
    
