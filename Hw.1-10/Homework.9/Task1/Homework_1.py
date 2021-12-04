hello = 'Hello file world!'
with open('myfile.txt', 'w') as file_object:
    file_object.write(hello)

with open('myfile.txt', 'r') as file_object:
    line_1 = file_object.read()

print(line_1)
