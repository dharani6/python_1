# Class Attribute and Instance Attributes


class Employee:
    No_of_working_Hrs = 40

emp_1 = Employee()
emp_2 = Employee()

print(emp_1.No_of_working_Hrs)
print(emp_2.No_of_working_Hrs)

Employee.No_of_working_Hrs = 50

print(emp_1.No_of_working_Hrs)
print(emp_2.No_of_working_Hrs)

emp_1.name = "ONE"  # Instance attribute
emp_2.name = "TWO"
print(emp_1.name, emp_2.name)