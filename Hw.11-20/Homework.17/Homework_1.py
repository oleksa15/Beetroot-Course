# coding = UTF-8

def with_index(iterable = 0, start = 0):
    list_0 = []
    if iterable == 0:
        return [(start, iterable)]

    for i in iterable:
        list_0.append((start, i))
        start += 1
    return list_0

a = ['rti', 'eoirf', 34, 13]
print(with_index(a))
