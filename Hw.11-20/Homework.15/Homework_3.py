# coding = UTF-8

def arg_rules(type_: type, max_length: int, contains: list):
    def search(func):
        def search_1(name):
            if type_ != type(name):
                return f'Create_slogan({name}) is False. Type error'
            elif not 0 < len(name) <= max_length:
                return f'Create_slogan({name}) is False. Length error'
            elif not is_in_list(name, contains):
                return f'Create_slogan({name}) is False. Contains error'
            return func(name)
        return search_1
    return search

def is_in_list(name: str, contains: list):
    for i in contains:
        if not i in name:
            return False
    return True

@arg_rules(type_ = str, max_length = 15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH'))
print(create_slogan(25))
print(create_slogan('S@SH05'))

