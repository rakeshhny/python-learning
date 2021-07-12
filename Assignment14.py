
class Student:
    def __init__(self, rollno, name, semester, branch):
        self.rollno = rollno
        self.name = name
        self.semester = semester
        self.branch = branch

    def getInputFromUser():
        rollno = int(input("Enter roll no:"))
        name = input("Enter student name:")
        semester = int(input("Enter student semester:"))
        branch = input("Enter student branch:")
        return Student(rollno, name, semester, branch)

    def displayStudentData(self):
        print("Student rollno =", self.rollno, "name =", self.name, "semester =", self.semester, "branch =", self.branch)


student1 = Student.getInputFromUser()
student1.displayStudentData()