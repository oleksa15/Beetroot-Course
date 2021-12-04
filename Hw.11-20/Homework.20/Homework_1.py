# coding = UTF-8

import logging
from os import path

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

class File(object):
    counter = 0

    @classmethod
    def get_counter(cls):
        return cls.counter

    def __init__(self, file_name, method):
        self.file_name = file_name
        self.method = method

    def __enter__(self):
        File.counter += 1
        self.file_obj = open(self.file_name, self.method)
        logging.warning(f'Opens the file and returns it: {File.counter}')
        return self.file_obj

    def __exit__(self, type, value, traceback):
        logging.warning(f'Closes the file: {File.counter}')
        self.file_obj.close()

def write(text_1: str, file_1: str):
    with File(file_1, 'a') as f_1:
        f_1.write(f'{text_1}\n')

def reads(file_2: str):
    if not path.isfile(file_2):
        raise FileNotFoundError(f'The file "{file_2}" does not exist')

    with File(file_2, 'r+') as f_2:
        a = f_2.read()
        return a

if __name__ == '__main__':
    write('One', 'demo.txt')
    reads('demo.txt')

    print(File.get_counter())