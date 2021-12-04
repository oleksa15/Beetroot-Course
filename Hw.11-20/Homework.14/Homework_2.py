# coding = UTF-8

def func1(a):

    def func2(b):
        nonlocal a
        a = 1
        return a + b

    return func2

f = func1(4)
print(f(6))
print(f(3))
