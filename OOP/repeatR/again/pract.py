class One:

    def __init__(self, a):
        self.a = a

    def func(self):
        return self.a ** 2


class Two:

    def __init__(self, a ,b):
        self.a = a
        self.b = b

    def func(self):
        return self.a * self.b
    

a1 = One(2)
a2 = Two(3, 4)

together = [a1, a2]

for i in together:
    print(i.func())
   

class Delegation:

    def bench(self):
        print('i can bench')

    def squat(self):
        print('i can squat')


class Bob(Delegation):

    def raw(self):
        super().bench()
        print('Bob can raw')
        super().bench()


a = Bob()
a.raw()

