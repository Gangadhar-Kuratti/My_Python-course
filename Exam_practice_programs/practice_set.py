# largest of three without using max()
lis=[10,20,30]
largest=lis[0]
for num in lis:
    if num>largest:
        largest=num
print(largest)    