# coding = UTF-8

import unittest
import Homework_14

class SquaresTestCase(unittest.TestCase):

    def test_squared(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8]
        l2 = Homework_14.square_nums(l)
        self.assertEqual(l2,  [1, 4, 9, 16, 25, 36, 49, 64])

    def test_remove_negatives(self):
        l = [1, -2, 3, 4, -5, 6, 7, -8]
        l3 = Homework_14.remove_negatives(l)
        self.assertNotEqual(l3,  [1, 3, 4, 6, 7])

unittest.main()