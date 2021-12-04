def add(a, b):
    try:
        a = int(a)
        b = int(b)
        print(a**2/b)
    except ZeroDivisionError:
        print("Не можливо ділити на нуль")
    except ValueError:
        print("Введіть будь ласка числа")

add(input('a = '), input('b = '))