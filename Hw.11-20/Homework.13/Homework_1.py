class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        return

    def simple_talk(self):
        self.talk()

class Cat(Animal):
    def talk(self):
        print('meow')

class Dog(Animal):
    def talk(self):
        print('woof woof')

a = Cat('Tom')
b = Dog('Spaik')
list1 = [a, b]

for animal in list1:
    animal.simple_talk()
