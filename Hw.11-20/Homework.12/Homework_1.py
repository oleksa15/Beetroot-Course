# coding = UTF-8

class Person():
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name


class Teacher(Person):
    def __init__(self, f_name, l_name, salary):
        super().__init__(f_name, l_name)
        self.salary = salary

    def display_teacher(self):
        return(f"Teacher. First name: {self.f_name}; Last name: {self.l_name}; Salary: {self.salary}")


class Student(Person):
    def __init__(self, f_name, l_name, notion):
        super().__init__(f_name, l_name)
        self.notion = notion

    def display_student(self):
        return(f"Student. First name: {self.f_name}; Last name: {self.l_name}; Notion: {self.notion}")


S = Student("C", "D", "10")
T = Teacher("A", "B", "500$")

print(S.display_student())
print(T.display_teacher())
