# coding = UTF-8

import random

m = 0

def quicksort(num_list, first, last):
    if first < last:
        size_arr = last - first + 1
        if size_arr < m:
            insert_sort(num_list, first, last)
            prin('Wow')
        else:
            mid = partition(num_list, first, last)
            quicksort(num_list, first, mid-1)
            quicksort(num_list, mid + 1, last)

def partition(num_list, first, last):
    piv = num_list[last]
    i = first - 1
    for j in range(first, last):
        if num_list[j] < piv:
            i += 1
            temp = num_list[i]
            num_list[i] = num_list[j]
            num_list[j] = temp

    tempo = num_list[i+1]
    num_list[i+1] = num_list[last]
    num_list[last] = tempo

    return i+1

def insert_sort(array, first, last):
    for index in range(first, last+1):
        current_value = array[index]
        position = index
        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position = position - 1

        array[position] = current_value


if __name__ == "__main__":
    test_list = [random.randint(1, 100) for _ in range(10)]
    print(test_list)
    copy_test_list = test_list[:]
    quicksort(copy_test_list, 0, len(copy_test_list) - 1)
    print(copy_test_list)