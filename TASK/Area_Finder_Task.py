

# Task 3: Area Finder


print("\n===============Area Finder===============\n")

def Circle(radius):
    return 3.14*radius*radius

def Triangle(hieght,base):
    return 0.5*hieght*base

def Rectangle(length,width):
    return length*width

print("\t 1.Circle \n\t 2.Triangle \n\t 3.Rectangle\n")
choice= int(input("\tEnter Your Choice: "))


if choice==1:
    radius=float(input("\n\tEnter Radius: "))
    print("\tArea of Circle is:",Circle(radius))
    print("\n\tThank You !!")

elif choice==2:
    hieght=float(input("\n\tEnter Hieght: "))
    base= float(input("\tEnter Base: "))
    print("\tArea of Triangle is:",Triangle(hieght,base))
    print("\n\tThank You !!")

elif choice==3:
    length=int(input("\n\tEnter Length: "))
    width=int(input("\tEnter Width: "))
    print("\tArea of Rectangle is:",Rectangle(length,width))
    print("\n\tThank You !!")

else:
    print("\tInvalid Choice...")

