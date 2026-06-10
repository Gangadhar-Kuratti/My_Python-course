# program to print the smallest number in the list

def smallest(numbers):
    small = numbers[0]
    for i in numbers:
        if i < small:
            small=i
    print(small)
smallest([1,2,3,4,5])
    
    