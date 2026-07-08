# Program to understand the methods

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(sum)

        avg=sum/len(self.marks)
        print(avg)

    
s1=Student("nikhil",[20,30,40])
s1.get_avg()


