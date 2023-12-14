

class Calculation:


    def display(self,x,y):

        self.n1=x
        self.n2=y

        print(f'x= {x}, y= {y}')


    def fact(self):

        f=1

        for i in range(1,self.n1+1):

            f*=i

        return f

    def add(self):

        print("Addition of two Number: ",self.n1+self.n2)


c1= Calculation()

c1.display(3,40)

print("3 Number of factorial is: ",c1.fact())

c1.add()
