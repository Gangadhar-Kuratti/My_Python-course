# program for single inheritance

class car:
    @staticmethod
    def start():
        print("Car started!")
    
    @staticmethod
    def stop():
        print("Car stopped..")

class toyatocar(car):
    def __init__(self,name):
        self.name=name

car1=toyatocar("fortuner")
print(car1.start())

# program for multi-level inheritance

class car:
    @staticmethod
    def start():
        print("Car started!")
    
    @staticmethod
    def stop():
        print("Car stopped..")

class toyatocar(car):
    def __init__(self,name):
        self.name=name

class brand(toyatocar):
    def __init__(self,name):
        self.name=name
    
car2=brand("land_cruiser")
print(car2.stop())

# program for multiple inheritance

class A:
    var_a="This is class A.."

class B:
    var_b="This is class B.."

class C(A,B):
    var_c="This is class C.."

C1=C()
print(C1.var_a) 
print(C1.var_b) 
print(C1.var_c) 