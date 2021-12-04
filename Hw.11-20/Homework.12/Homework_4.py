# coding = UTF-8

class CustomException(Exception):
    def __init__(self, num, msg="Number is not in range from 5,000 to 15,000. Number"):
        self.num = num
        self.msg = msg
        super().__init__(self.msg)

        with open('logs.txt', 'a') as file_object:
            file_object.write(f'{self.msg} is {self.num}\r\n')


try:
    number1 = int(input("Enter number: "))
    if not 5000 < number1 < 15000:
        raise CustomException(number1)
except CustomException:
    print("[ERROR]")
