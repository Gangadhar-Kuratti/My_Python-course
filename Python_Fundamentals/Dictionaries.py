# program to understand the concept of dictionary

dictionary={"nikhil":"1-1-2008",
           "class":"10th",
           "section":"2"}

# program to understand dictionary methods

print(dictionary.keys())    # prints all the keys attributes

print(dictionary.values())  # prints value attributes

print(dictionary.items())   # prints all the items

# program for operations of dictionary

print(dictionary["class"])  # accessing the elements of dictionary

dictionary["class"]="std"   # updating the dictionary elements
print(dictionary)

dictionary.pop("nikhil")    #deleting operation
print(dictionary)

del dictionary["section"]   # deleting operation 
print(dictionary)

