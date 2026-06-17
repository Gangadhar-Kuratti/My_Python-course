# program to detect the spaces in a string
def detect(sentence):
    count = 0

    for i in sentence:
        if i == " ":
            count += 1

    return count

print(detect("I love python"))