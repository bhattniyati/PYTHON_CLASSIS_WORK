# Heirarchical Inheritance:

class A:

    def add(self,a1,a2):

        self.num1=a1
        self.num2=a2

    def displayA(self):

        print("Addition of Two Number is: ",self.num1+self.num2)


class B(A):

    def sub(self,n1,n2):

        self.no1=n1
        self.no2=n2

    def displayB(self):

        print("Substraction of Two Number is: ",self.no1+self.no2)


class C(A):

    def mul(self,x1,x2):

        self.n1=x1
        self.n2=x2

    def displayC(self):

        print("Multiplication of Two Number is: ",self.n1*self.n2)


b1= B() # Object 1 of class B
c1= C() # Object 2 of class C

b1.add(10,20)
b1.displayA()

b1.sub(50,25)
b1.displayB()

c1.add(30,40)
c1.displayA()

c1.mul(10,4)
c1.displayC()
