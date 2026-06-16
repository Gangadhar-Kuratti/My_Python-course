# program to count the words in sentence

def words(sentence):
    count=0
    for word in sentence.split():
        count+=1
    print(count)
words("HI hi hi")

# program to count the words in sentence using return() function

def words(sentence):
    return len(sentence.split())
print(words("HI hi HI hi"))