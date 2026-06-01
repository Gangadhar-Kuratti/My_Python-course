# program to count the vowels in a entered string
count=0
string=input("Enter string: ").lower()
for s in string:
    if s=="a" or s=="e" or s=="i" or s=="o" or s=="u":
        count+=1
print(count)

# program to print the sum of even numbers

sum=0
for i in range(1,51):
    if i%2==0:
        sum+=i
print(sum)

# program to print the entered character along with its index

string=input("Enter string: ")
for index,i in enumerate (string):
    print(index,i)

# program to print the factorial of number

fact=1
num=int(input("Enter number: "))
for i in range(1,num+1):
    fact=fact*i
print(fact)

# program to count the even and odd number

even_count=0
odd_count=0
for i in range(1,101 ):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("even numbers between 1-100 :",even_count)
print("Odd numbers between 1-100: ",odd_count)

# program to reverse the entered string

string = input("Enter string: ")

reverse = ""

for i in range(len(string)-1,-1,-1):
    reverse += string[i]

print(reverse)


