# Program to understand the abstration

class car:
    def __init__(self):
        self.acc=False
        self.clutch=False
        self.brk=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("Car started")

c1=car()
c1.start()
