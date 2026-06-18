def second_largest(numbers):

    largest = numbers[0]
    second = numbers[0]

    for i in numbers:

        if i > largest:
            second = largest
            largest = i

        elif i > second and i != largest:
            second = i

    print(second)

second_largest([10, 50, 30, 20])