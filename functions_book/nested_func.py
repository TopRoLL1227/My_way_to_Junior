# Вкладена функція 


a = 'AUDI'
b = 'BMW'
m = 'MERCEDES'


def car1():
    print(a)

car1()


def car2():
    def car3():
        print(b)
    return car3()

car2()


def car3():
    def car4():
        def car5():
            print(m)
        car5()
    car4()

car3()


a = 3

def work():
    asd = 1
    def next_work():
        def finish_work(a=13):
            print(a)
        return finish_work()
    return next_work()

work()  # 13
print(a)  # 3

#########################################################
first = 1
second = 2
third = 3

def numbers():

    def one():
        o = 'one'
        print(o, first)

    def two():
        t = 'two'
        print(t, second)

    def three():
        th = 'three'
        print(th, third)
    
    one()
    two()
    three()

numbers()

def one():
    a = 1
    def two():
        a = 2
        def three():
            a = 3
            print(a)
        three()
        print(a)
    two()
    print(a)

one()