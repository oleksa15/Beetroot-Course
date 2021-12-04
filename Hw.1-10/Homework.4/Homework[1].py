from random import randint
number = randint(1, 10)
user_number = int(input("Спробуйте вгадати число від 1 до 10 :"))
if user_number == number:
    print("You win")
elif user_number != number:
    print("Game Over")
else:
    print("Error")
