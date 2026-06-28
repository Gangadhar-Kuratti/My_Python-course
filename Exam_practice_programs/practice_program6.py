from array import * # Creating an array to store temperatures of 7 days 
temperature = array('i', [32, 35, 30, 28, 34, 36, 31]) 
print("Daily Temperature Record (in °C):") 
for i in range(len(temperature)): 
    print("Day", i + 1, "Temperature =", temperature[i]) 
    print("\n--- Indexing Example ---") # Accessing temperatures using indexing 
    print("Temperature on Day 1 =", temperature[0], "°C") 
    print("Temperature on Day 4 =", temperature[3], "°C") 
    print("Temperature on Last Day =", temperature[-1], "°C") 
    print("\n--- Slicing Example ---") # Accessing temperatures using slicing 
    print("First 3 days temperature =", temperature[:3]) 
    print("Middle 3 days temperature =", temperature[2:5]) 
    print("Last 2 days temperature =", temperature[-2:]) 
    print("\n--- Highest Temperature Check ---") # Sorting to find highest temperatures 
    sorted_temp = array('i', sorted(temperature, reverse=True)) 
    print("Top 3 highest temperatures =", sorted_temp[:3]) 