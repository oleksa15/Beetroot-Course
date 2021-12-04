from random import randint
numbers1 = []
numbers2 = []
for i in range (0,10):
    numbers1.append(randint(1,10))
    numbers2.append(randint(1, 10))
print(numbers1)
print(numbers2)
numbers3 = list(set(numbers1) & set(numbers2))
print(numbers3)
