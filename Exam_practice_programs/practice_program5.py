text = input("Enter a string: ")     
reverse = ""     
for ch in text:         
    reverse = ch + reverse     
    if text == reverse:         
        print("Palindrome String")     
    else:         
        print("Not Palindrome String") 
else:     
        print("Invalid choice") 