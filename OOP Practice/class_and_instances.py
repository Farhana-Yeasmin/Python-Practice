
# class Employee:
#     pass
#
# emp_1 = Employee()
# emp_2 = Employee()
#
# emp_1.firstName = "Farhana"
# emp_1.lastName = "Yeasmin"
#
# emp_2.firstName = "Bulbul"
# emp_2.lastName = "Ahmed"
#
# print(emp_1.firstName)
# print(emp_2.firstName)


class Employee:

    num_of_emp = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'+last+'@company.com'

        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1 = Employee('Farhana','Yeasmin',20000)
emp_2 = Employee('Bulbul','Ahmed',40000)

# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())

print(Employee.num_of_emp)