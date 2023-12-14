
class Abc:

    def data(self,a,b):
        
        self.x= a
        self.y= b

    def display(self):

        print(f'a={self.x}, b={self.y}, \nMultiplication of two number is: {self.x*self.y}')


class Language:

    def Language_types(self,l1,l2):

        self.l1=l1
        self.l2=l2

    def display(self):

        print("\nTypes of Language: ")
        print("Type 1:", self.l1)
        print("Type 2:", self.l2)

o1= Abc()

o1.data(10,20)
o1.display()
        

l1= Language()

l1.Language_types("Python","Java")
l1.display()
