# Multi-Level:


class A:

    def displayA(self):

        print("Hello From Class A..")

class B(A):

    def displayB(self):

        print("Hello From Class B..")

class C(B):

    def displayC(self):

        print("Hello From Class C...")
    

c1= C()

c1.displayA()
c1.displayB()
c1.displayC()
