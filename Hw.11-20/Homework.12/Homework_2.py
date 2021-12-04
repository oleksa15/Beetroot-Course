# coding = UTF-8

from calendar import isleap


class Mathematician:

    def square_nums(self, *args):
        squared = []
        for i in args:
            squared.append(i**2)
        return squared

    def remove_positives(self, *args):
        removed = [i for i in args if i < 0]
        return removed

    def filter_leaps(self, *args):
        filtered = [i for i in args if isleap(i)]
        return filtered


m = Mathematician()

print(m.square_nums(7, 11, 5, 4))
print(m.remove_positives(26, -11, -8, 13, -90))
print(m.filter_leaps(2001, 1884, 1995, 2003, 2020))
