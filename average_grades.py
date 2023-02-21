# class_average.py
"""Average program with seauence ocntroll iteration"""

# initialization phase
total = 0
grade_counter = 0;
grades = [98, 78, 67, 56, 34, 56, 89, 90, 34, 56, 68]

# processing phase
for grade in grades:
    total += grade
    grade_counter += 1

average = total / grade_counter
print(f'Class average is:{average}')

# class average sentinel
"""Class average with sentinel controlled iteration"""
# initialization phase
total = 0
grade_counter = 0
grade = int(input("Enter grade, type -1 to end it:"))

# processing phase
while grade != -1:
    total += grade
