# coding = UTF-8

class Dog:
    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        print(f"Dog is {self.dog_age * 7} year old")


dog_1 = Dog(3)
dog_1.human_age()
