# program to print the pyramid star pattern

rows=5
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()

# program to print the number pattern

rows=5
for i in range(rows+1):
    for j in range(i):
        print(j+1,end=" ")
    print()