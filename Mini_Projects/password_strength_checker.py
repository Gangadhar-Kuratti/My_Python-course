def check_password(password):

    length_check = len(password) >= 8
    uppercase_check = False
    lowercase_check = False
    number_check = False
    symbol_check = False

    for char in password:

        if char.isupper():
            uppercase_check = True

        elif char.islower():
            lowercase_check = True

        elif char.isdigit():
            number_check = True

        else:
            symbol_check = True

    score = 0

    if length_check:
        score += 1

    if uppercase_check:
        score += 1

    if lowercase_check:
        score += 1

    if number_check:
        score += 1

    if symbol_check:
        score += 1

    print("\n===== PASSWORD CHECK =====")

    print("Length (8+):", "Yes" if length_check else "No")
    print("Uppercase  :", "Yes" if uppercase_check else "No")
    print("Lowercase  :", "Yes" if lowercase_check else "No")
    print("Number     :", "Yes" if number_check else "No")
    print("Symbol     :", "Yes" if symbol_check else "No")

    if score == 5:
        print("\nPassword Strength: Strong")
    elif score >= 3:
        print("\nPassword Strength: Medium")
    else:
        print("\nPassword Strength: Weak")


print("===== PASSWORD STRENGTH CHECKER =====")

password = input("Enter your password: ")

check_password(password)