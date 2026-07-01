# program for class and objects

class Human:
    def __init__(self,name):
        self.name=name
        
    def read(self):
        print(f"{self.name} is reading")
    
person1=Human("person1")
person2=Human("Person2")

person1.read()

