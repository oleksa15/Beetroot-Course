# coding = UTF-8

import timeit

def fibonacci_generator(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_generator(n - 1) + fibonacci_generator(n - 2)


def fibonacci_search(arr, x):
    m = 0
    while fibonacci_generator(m) < len(arr):
        m = m + 1
    offset = -1
    while fibonacci_generator(m) > 1:
        i = min(offset + fibonacci_generator(m - 2) , len(arr) - 1)
#        print(f'Current element {i}: {arr[i]}')
        if x > arr[i]:
            m = m - 1
            offset = i
        elif x < arr[i]:
            m = m - 2
        else:
            return i
    if fibonacci_generator(m - 1) and arr[offset + 1] == x:
        return offset + 1
    return -1

#print('Number found at index : ', fibonacci_search([-100, -1.5, 2, 3, 4, 6, 31, 101], 6))

def sequential_search(array, item):
    pos = 0
    found = False
    while pos < len(array) and not found:
        if array[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


def binary_search(array, item):
    first = 0
    last = len(array) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if array[midpoint] == item:
            found = True
        else:
            if item < array[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found