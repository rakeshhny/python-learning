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

# Sort the list of employees in the ascending order of name
employees.sort(key=lambda x: x.name, reverse=False)

print("Employees in the ascending order of name")
for emp in employees:
    emp.showEmpData()

# sort the list of employees in descending order or salary
employees.sort(key=lambda x: x.salary, reverse=True)

print("Employees in the descending  order of salary")
for emp in employees:
    emp.showEmpData()