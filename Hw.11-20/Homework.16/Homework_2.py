# coding = UTF-8

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def __repr__(self):
        return f'({self.id}, {self.name}, {self.company})'

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, obj):
        if not isinstance(obj, Worker):
            raise TypeError('WorkersError')
        else:
            self._workers.append({'id': obj.id, 'name': obj.name, 'company': obj.company})

class Worker:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.company}, {self.boss}'

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if not isinstance(new_boss, Boss):
            raise TypeError('Boss error')
            return

        if self._boss:
            temp_1 = next((a for a in self._boss.workers if a['id'] == self.id), None)
            if temp_1:
                self._boss.workers.remove(temp_1)
        new_boss.workers = self
        self._boss = new_boss

b1 = Boss(1, 'Alex', 'oeor')
b2 = Boss(2, 'Ban', 'rfr')
w1 = Worker(1, 'Candy', 'erf')
w2 = Worker(2, 'D', 'A')
w3 = Worker(3, 'Erika', 'Deutche')
w1.boss = b1
w2.boss = b1
w3.boss = b1
print(b1.workers)
print(b2.workers)
w2.boss = b2
print(b1.workers)
print(b2.workers)
