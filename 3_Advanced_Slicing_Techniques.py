#Task 1: 
#Given:
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week = temperatures[7:14] #create a new list with the contents from the 2nd week of temperatures

print(second_week) #print outcome for user

#Task 2:

start_index = temperatures.index(100) #save index of value 100
start_index += 1 #move index value up by one to get values above 100

above_100 = temperatures[start_index:] #slice the list at new starting index til the end to capture all values above 100

print(above_100) #display outcome of slice to user