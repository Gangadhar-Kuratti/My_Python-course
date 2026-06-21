# program to count the appearence of a character

def appearence(text,ch):
    count=0
    for i in text:
        if i==ch:
            count+=1
    print(count)
    
appearence("HIHHHH","H")