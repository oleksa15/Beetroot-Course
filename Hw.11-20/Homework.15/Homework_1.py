# coding = UTF-8

def our_decorator(func):
    def function_wrapper(*args):
        print(f'Function name is {func.__name__} and arguments {args}')
    return function_wrapper

@our_decorator
def foo(x):
    print("It is " + x)

foo(42, 'dfgh')
