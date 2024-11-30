#Practical : 22- Write a python program that import different packages.

# import the student class defined in the check_practical22.py file 
from check_practical22 import student
student_name = input("Enter student name:")
student_branch = input("Enter student branch:")

std = student(student_name,student_branch)
std.get_data()

