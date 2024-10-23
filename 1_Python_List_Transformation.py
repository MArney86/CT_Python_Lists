#Task 1: 
#Given:
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort() #sort list by ascending order
grades.reverse() #reverse order to descending order
print(grades) #display the reorganized list

#Task 2:

total_sum = 0
for grade in grades:
    total_sum += grade #add all the values in the list
average =  total_sum / len(grades) #divide by the number of items in the list
print(f"The average is {average}.") #display the average
