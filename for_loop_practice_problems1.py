# program to understand the list comprehension

l=[x for x in range(1,11)]
dl=[x**2 for x in l]
print(dl)

#program to understand the dictionar comprehension

names=["anand","geetha","kumar"]
d={name:len(name) for name in names}
print(d)