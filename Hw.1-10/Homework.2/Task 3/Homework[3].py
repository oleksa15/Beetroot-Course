num1 = int(input("Введіть перше число :"))
oper = str(input("Введіть знак :"))
num2 = int(input("Введіть друге число :"))
if oper == "+" :
    print(num1 + num2)
elif oper == "-" :
    print(num1 - num2)
elif oper == "*" :
    print(num1 * num2)
elif oper == "/" :
    print(num1 / num2)
elif oper == "**" :
    print(num1 ** num2)
elif  oper == "//" :
    print(num1 // num2)
else :
    print("Error")
