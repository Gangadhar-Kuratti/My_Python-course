# program to understand the encapsulation 
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc

    def credit(self,amount):
        self.balance+=amount
        print(f"{amount} was credited")
        print(self.balance)

    def debit(self,amount):
        self.balance-=amount
        print(f"{amount} was debited")
        print(self.balance)

u1=Account(10000,12345)
u1.credit(2000)
u1.debit(3000)