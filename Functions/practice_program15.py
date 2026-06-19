# program to count the digits,letters and special characters

def characters(character):
    count_digit=0
    count_alphabet=0
    count_specialchar=0
    for i in character:
        if i.isalpha():
            count_alphabet+=1
        elif i.isdigit():
            count_digit+=1
        else:
            count_specialchar+=1
    print(f"number of alphabets is {count_alphabet}")
    print(f"number of digits is {count_digit}")
    print(f"number of special characters is {count_specialchar}")
characters("Nik28@")