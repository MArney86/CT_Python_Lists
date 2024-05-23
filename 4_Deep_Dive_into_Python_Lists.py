#Given:

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

#task 1:

below_80 = [] #empty list to store filtered students(s)
for grade in grades: #iterate the students by grade
    if grade < 80: #test if grade is less than 80
        below_80.append(students[grades.index(grade)]) #add values at corresponding indexes to filtered list 
        below_80.append(grade)
        below_80.append(activities[grades.index(grade)])
    else:
        pass

print(below_80) #print the results of the filterint to the user

#Task 2: 
student_approved = [] #create list named student_approved to store names of approved students
for student in students: #iterate the list of students
    if student not in below_80: #test if student is not in the filtered list
        student_approved.append(student) #add student name to student_approved if not filtered
    else:
        pass

#Task 3:
print(student_approved) #print the student_approved list