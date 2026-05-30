# list comprehension for even square numbers

l=[x for x in range(1,11)]
dl=[x**2 for x in l if x%2==0]
print(dl)

# program to understand split() function

z=input("Enter list of integers: ").split()
print(z)
y=[int(num) for num in z]
print(y)