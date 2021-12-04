# coding = UTF-8

'''

Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

def stop_words(words: list):

    pass

@stop_words(['pepsi', 'BMW'])

def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"



assert create_slogan("Steve") == "Steve drinks * in his brand new *!"


'''

def censured_words(words: list):
    def search(func):
        def search_1(name):
            a = func(name)
            for word in words:
                a = a.replace(word, '*')
            return a
        return search_1
    return search


@censured_words(['meat'])
def text(name: str) -> str:
    return f"{name} eat meat"

print(text("A"))
