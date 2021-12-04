str_ = input("Ввведіть рядок :")

if len(str_) < 2:
    print()
else:
    result = str_[:2] + str_[-2:]
    print(result)