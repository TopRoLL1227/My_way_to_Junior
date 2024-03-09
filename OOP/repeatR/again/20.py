from time import perf_counter

class Counter:

    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.lenght = 0
        print('init object')

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.lenght += len(args)
        print(f'this exemplar callable {self.counter}')

    def average(self):
        return self.summa / self.lenght


b = Counter()
print(b)

b(3, 4, 5)
print(b.summa)
print(b.lenght)
print(b.average())




