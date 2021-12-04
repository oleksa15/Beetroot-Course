import unittest
import Homework_1
import logging

class TestTaskOne(unittest.TestCase):

    def test_add(self):
        file_test = 'demo.txt'
        test_text = f'Two\n'
        Homework_1.write(test_text, file_test)
        with open(file_test, 'r+') as f_1:
            a_1 = f_1.readline()
        self.assertEqual(test_text, a_1)
