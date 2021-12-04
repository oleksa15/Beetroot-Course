def make_operation(operation, a, b) -> str:
    c = a * b
    if operation == '+':
        print(c)
    return(str(c))
print(make_operation(' * ', 7, 6))
