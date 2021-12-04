# coding = UTF-8

class InRange:
    def __init__(self, _start, _end, step=1):
        self.ind = _start
        self.to = _end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind > self.to -1:
            raise StopIteration
        val = self.ind # ** 2
        self.ind += self.step
        return val

a = InRange(1, 10)

list_1 = []
for i in a:
    list_1.append(i)
print(list_1)