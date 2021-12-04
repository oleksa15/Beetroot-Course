from random import randint
numbers = []
for i in range (0,10):
    numbers.append(randint(0,100))
integers = [x for x in numbers if x % 7 == 0 and x % 5]
print(integers)