# program  to print the even numbers using while loop

is_failed=True
i=1
while is_failed:
    if i%2!=0:
        i+=1
        continue
    print(i)
    i+=1
    if i>10:
        break

# program to print the odd numbers using while loop

i=1
while i<=10:
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=1
    
# program for small ATM application using while loop and if condition

pin="1234"
i=1
while i<=3:
    pin_input=input("Enter password: ")
    i+=1
    if pin_input==pin:
            print("Correct")
            break
    else:
            print("Incorrect")
            
# program to guess the 1correct the number

number=7
while True:
    num=int(input("Enter number: "))
    if num<number:
            print("LITTLE HIGHER")
    elif num>number:
            print("LITTLE LOWER")
    else:
        print("CORRECT")
        break