# coding = UTF-8

import random

def shaker_sort(array):
    n = len(array)
    swapped = True
    start = 0
    end = n - 1

    while swapped is True:

        swapped = False
        for k in range(start, end):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
                swapped = True
        if not swapped:
            break

        swapped = False

        end -= 1
        for l in range(end - 1, start-1, -1):
            if array[l] > array[l + 1]:
                array[l], array[l + 1] = array[l + 1], array[l]
                swapped = True

        start += 1


if __name__ == "__main__":
    test_list = [random.randint(1, 100) for _ in range(10)]
    print(test_list)
    copy_test_list = test_list[:]
    shaker_sort(copy_test_list)
    print(copy_test_list)
