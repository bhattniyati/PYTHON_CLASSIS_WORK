

class Sample:

    # class members

    num=90

    #self is default argument for class methods
    # self reprsents current class

    def add(self):
        print("Addition: ",self.num+20)

    def multi(self):
        print("Multiplication: ",self.num*10)

# Object Creation

s1= Sample()

s1.add()
s1.multi()


print("Outside of class")
print("Number= ",s1.num)
