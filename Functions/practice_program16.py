# program to print the longest word in entered string

def longest(sentence):
    s= sentence.split()
    large=s[0]
    for i in s:
        if len(i)>len(large):
            large=i
    print(large)
longest("Hi There Iam Learning Python")