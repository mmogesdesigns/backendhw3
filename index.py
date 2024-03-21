# The aim of this assignment is to practice advanced list operations and transformations.

# Problem Statement:
# You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.

# Task 1: Given the list of grades:

# grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# Sort the grades in descending order and display the sorted list.

# Task 2: Calculate the average grade and display it.

# Task 3: Replace any grade below 80 with the value Failed.
grades =  [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

print(grades)
grades.sort(reverse=True)
print(grades)

sum_of_grades = sum(grades)
print(sum_of_grades)
print(sum_of_grades)

average_grade = sum_of_grades / len(grades)
print(average_grade) 

print("The average grade is: ", + average_grade)


for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "Failed"

print("Modified list of grades:", grades)
#2
# The aim of this assignment is to delve deeper into list methods and understand the nuances of identity operators.

# Problem Statement:
# You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

# Task 1: Given the two lists:

# submitted = ["Alice", "Bob", "Charlie", "David"]
# attended = ["Charlie", "Eve", "Alice", "Frank"]
# Find out which students both submitted their assignments and attended the class.

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

common_students = []

for student in submitted:
    if student in attended:
        common_students.append(student)
print("Common students, ",common_students)

submitted_sorted = sorted(submitted)
print(submitted_sorted)
attended_sorted = sorted(attended)
print(attended_sorted)

identical_list = submitted_sorted == attended_sorted
if identical_list:
    print("The lists are identical")
else:
    print("The lists are not identical")

attended_copy = attended.copy()

for student in attended:
    if student not in submitted:
        attended_copy.remove(student)
print(attended_copy)
#3
# Task 1: Given the list of temperatures:

# temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
# Extract the temperatures for the second week (7 days) of the month. Expected Outcome: 83, 85, 86, 87, 88, 89, 90,

# Task 2: Extract all the temperatures above 100.

# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week_temp = temperatures[7:14]
print(second_week_temp)

above_100_temp = []
for temp in temperatures:
    if temp > 100:
        above_100_temp.append(temp)
print("temperatures above 100:", above_100_temp)

reversed_temp = temperatures[::-1]
extracted_temp = reversed_temp[4:10]
print("extracted temps from reversed list: ", extracted_temp)
#4
# Objective:
# The aim of this assignment is to integrate various list operations and methods to solve a complex problem.

# Problem Statement:
# You're organizing a school event, and you have lists containing student names, their grades, and the activities they're interested in.

# Task 1: Given the lists:

# students = ["John", "Doe", "Jane", "Smith"]
# grades = [85, 90, 78, 88]
# activities = ["Football", "Music", "Art", "Dance"]
# Filter out students who have grades below 80. Print the name, grade and activiy. Expected Outcome "Jane", 78, "Art"

# Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]


students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

for i in range(len(students)):
    if grades[i]< 80:
        print(students[i],grades[i],activities[i])

students_approved = []
for i in range(len(students)):
   if grades[i] >= 80:
       students_approved.append(students[i])
print("approved students: ", students_approved)