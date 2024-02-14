class Repeat:

    def say_hello(self, n):
        print(f'Hello my {self.name}, {self.n}')


a = Repeat()
a.name = 'ksu'
a.say_hello(1)
