

from threading import Thread


class Counter(Thread):
    counter = 0
    rounds = 100_000

    def __init__(self) -> None:
        Thread.__init__(self)

    def run(self) -> None:
        for _ in range(Counter.rounds):
            Counter.counter += 1


if __name__ == '__main__':
    counter_1 = Counter()
    counter_1.start()
    count_1 = Counter.counter

    counter_2 = Counter()
    counter_2.start()
    count_2 = Counter.counter

    print(count_1, count_2)