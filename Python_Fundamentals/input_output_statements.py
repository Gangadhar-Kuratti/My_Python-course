# program to understand input statements

Name=input("Enter your name: ")
Age=int(input("Enter your age: "))

print("Entered Name is " + Name + " and their respective age is " + str(Age))

# program to understand formated string concatination

Boy_name=input("Enter Boy name : ")
Boy_age=int(input("Enter Boy age : "))
Girl_name=input("Enter Girl name : ")
Girl_age=int(input("Enter Girl age : "))

# Here in 16th line 'abs' is absolute that converts -ve to +ve when user enters girls age > boy age
Age_differece=abs(Boy_age-Girl_age)

print(Boy_name + " is a friend of " + Girl_name + " and their age difference is "+ str(Age_differece ))

print(f"{Boy_name} is a friend of {Girl_name} and their age difference is {Age_differece}")  # formated string