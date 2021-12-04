# coding = UTF-8

import re

class Email:
    def __init__(self, email):
        self.email = self.validate(email)

    def validate(self, email):
        if (re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", email)):
            print(f'SUCCESSFULLY')
            return email
        else:
            print(f"ERROR")

Email('oleksaagmailcom.ua')
Email('oleksaa@gmail.com.ua')
Email('oleksaa@gmailcom')
Email('oleksaa@gmail.com')