# program to understand the array slicing and array indexing 

from array import *
temperature=array('i',[28,29,30,35,39,37,40])
for i in range (len(temperature)):
    print("Day-",i+1,"Temperature-",temperature[i],"Degree celsius")


print("-----Array indexing-----")
print("Temperature of 1st day was:",temperature[1])
print("Temperature of last day was:",temperature[6])


print("-----Array slicing-----")
print("Temperature of 1st three days were:",temperature[:3])
print("Temperature of last three days were:",temperature[4:7])
print("THESE WERE THE TEMPERATURES RECORDED FOR THE WEEK")