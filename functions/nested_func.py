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
        return car5()
    return car4()

car3()


a = 5

def zminna():
    def new_zminna():
        def way():
            print(a)
        return way()
    return new_zminna()

zminna()



asd = 1

def my_pract():
    def add_pract():
        def new_pract():
            print(asd)
        return new_pract()
    return add_pract()

my_pract()



asd = 2

def work():
    asd = 1
    def next_work():
        def finish_work(a=13):
            print(a)
        return finish_work()
    return next_work()

work()
print(asd)