class Employee:
    def __init__(self, empid, name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary

    def acceptEmpData():
        empid = int(input("Enter employee id:"))
        name = input("Enter employee name:")
        salary = int(input("Enter employee salary"))
        return Employee(empid, name, salary)

    def showEmpData(self):
        print("Employee empid =", self.empid, "name =", self.name, "salary =", self.salary)


employees = []

for i in range(1, 3):
    emp = Employee.acceptEmpData()
    employees.append(emp)

for emp in employees:
    emp.showEmpData()
