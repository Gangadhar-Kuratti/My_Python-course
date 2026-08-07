# create a class(2dvector) and use it to create a class representing a 3D vector

class twoDVector():
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"2D vector is {self.i}i + {self.j}j")

class threeDVector(twoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"3D vector is {self.i}i + {self.j}j + {self.k}k")
a=twoDVector(2,3)       
b=threeDVector(2,3,4)  
a.show() 
b.show()   

# create a class pet from class animal and further create a class dog from pets and add bark method to class dog

class animal():
    pass

class pets(animal):
    pass

class dog(pets):
    @staticmethod
    def bark():
        print("bow bow!")

a=dog()
a.bark()

        