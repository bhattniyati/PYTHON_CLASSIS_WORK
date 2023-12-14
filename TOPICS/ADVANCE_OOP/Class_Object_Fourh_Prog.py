
# Dunder/Magic Method:


class Info:


    # __init__(): Call automatically when object of class is created..

    def __init__(self,Name,Age):

        self.v1=Name
        self.v2=Age

    def display(self):

        print(f'Name={self.v1} \nAge={self.v2}')


    # __str__(): Call automatically & return string when object is created..
    
    def __str__(self):

        return "Hello All !! How Are You?"


I1= Info("Niyati",20)
I1.display()

print(I1)




    
