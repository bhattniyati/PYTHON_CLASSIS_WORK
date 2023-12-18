# Multiple:


class A:

    def name(self,name):

        self.n1=name

    def displayA(self):

        print("Your Name is: ",self.n1)

class B(A):

    def age(self,age):

        self.a1=age

    def displayB(self):

        print("Your Age is: ",self.a1)


class C(A):

    def sub(self,subject):

        self.s1=subject

    def displayC(self):

        print("Your Subject is: ",self.s1)

class D(B,C):

    def mark(self,marks):

        self.m1=marks

    def displayD(self):

        print("Your Marks is: ",self.m1)


d1= D()

d1.mark(75)
d1.displayD()
d1.sub("Python")
d1.displayC()
d1.age(20)
d1.displayB()
d1.name("ABC")
d1.displayA()
