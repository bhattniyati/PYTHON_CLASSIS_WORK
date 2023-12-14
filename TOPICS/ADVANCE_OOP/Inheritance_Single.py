

class Person:

    def displayP(self):

        print("Hello From Parent...")



# Inherit person class to student class

class Student(Person):

    def displayC(self):

        print("Hello From Child..")


s1= Student()
s1.displayC()
s1.displayP()
