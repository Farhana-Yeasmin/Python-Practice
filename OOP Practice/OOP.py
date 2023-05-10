class Person:
    def __init__(self, person_name: str, year_of_birth: int, ht: int = None):
        self.__name = person_name
        self.__year_of_birth = year_of_birth
        self.__height = ht
        self.abc = None

    def get_year_of_birth(self):
        return self.__year_of_birth

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if (self.__has_any_number(new_name)):
            print("Sorry person name cann't have number")
            return
        self.__name = new_name

    # use __ before any method or attributes mean that is only accessable internally.
    def __has_any_number(self, string):
        return "0" in string

    def get_summery(self):
        return f"Name: {self.__name}, DOB: {self.__year_of_birth}, Height: {self.__height}"


person_list = [Person("Farhana", 1998, 75),
               Person("Farh", 1800),
               Person("Farhana", 1993, 75),
               Person("Farhana", 1945, 85)]


# for person in person_list:
#     if person.get_year_of_birth() >= 1900:
#         print(person.get_summery())
#

# a_person = Person("Farhana", 1998, 5)
# print(a_person.get_summery())
#
# a_person.set_name("Yeasmin")
# print(a_person.get_summery())
#
# a_person.set_name("0Farhana")
# print(a_person.get_summery())


class Student(Person):
    def __init__(self, person_name: str, year_of_birth: int, email_id: str, student_id: str):
        super().__init__(person_name, year_of_birth)
        self.id = student_id
        self.email = email_id

    def get_summery(self):
        return f"Name:{self.get_name()} , Email: {self.email}, Birth: {self.get_year_of_birth()}"

    def __str__(self):
        return self.get_summery()


student = Student("S", 2000, "a@google.com", "1235asdasdsad")
student.set_name("Farhana")


# print(student.get_summery())
# print(student)

class Teacher(Person):
    def __init__(self, person_name: str, year_of_birth: int, dept: str):
        super().__init__(person_name, year_of_birth)
        self.dept = dept

    def get_summery(self):
        return f"{self.get_name()} is a Teacher"


new_person_list = [
    Person("Farhana", 1990),
    Student("St", 2300, "sd@gmailcom", "stid"),
    Teacher("S", 2600, "tid")
]

for p in new_person_list:
    # print(p.get_name())
    print(p.get_summery())


# When we just want to save some data then use struct
# When we don't need the function just need to save data
class PlainClass:
    pass


abc = PlainClass()
abc.age = 23
abc.name = "Farhana"


print(abc.age)