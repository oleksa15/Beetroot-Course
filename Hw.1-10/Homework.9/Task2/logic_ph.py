# coding = UTF-8
import methods_ph
data_book = methods_ph.opened()
instruction = ("For start type 'open'\n\
For exit type 'exit'\n\
For read type 'read'\n\
For add type 'add'")

while True:
    print(instruction)
    user_choice = input('Type what u want to do: ')
    if user_choice == 'open':
        methods_ph.opened()
        print("Phonebook was opened successfully")
    elif user_choice == 'read':
        methods_ph.read(data_book)
    elif user_choice == 'add':
        methods_ph.add(data_book)
    elif user_choice == 'exit':
        print("Goodbye!")
        break
    else:
        print("No such function")
        continue

