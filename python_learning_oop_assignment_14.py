# Exercise

# Define a class Student
# With instance variable names below
# rollno, name, semester, branch

class Student:

    def __init__(self, name):
        self.name = name;



name = input("Enter student name:")
s1 = Student(name)
print("Student name is",s1.name)
