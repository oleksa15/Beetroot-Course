import random
word = list(input("Введіть ваше слово:"))
for i in range(0, 5):
    random.shuffle(word)
    print(word)
