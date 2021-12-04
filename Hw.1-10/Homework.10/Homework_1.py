# coding = UTF-8

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"My name is {self.name} and I'm {self.age} year old")


person1 = Person("Oleksa", 15)
person1.talk()
