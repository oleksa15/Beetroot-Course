import random
b = random.randint(1, 100)
c = random.randint(1, 100)
a = b + c
d = int(input(f"Вирішіть приклад {b} + {c} :"))
if d == a:
    print("You Win")
else:
    print("You Lose")
