# Check if an employee has achieved his weekly target or not

class Employee:
    name = "Dharani"
    designation = "Sale Executive"
    salesmadeThisWeek = 6

    def hasAchivedTarget(self):
        if self.salesmadeThisWeek >= 5:
            print("Target as achived")
        else:
            print("Target has not been achived")


employee1 = Employee()
print(employee1.name)
employee1.hasAchivedTarget()
