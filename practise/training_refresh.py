def inner_func(a, b):
    def add():
        print(a + b)
        a()
        b()
    return add

def say_hello():
    print('Hello')

def say_world():
    print('World')


say_hello = inner_func(say_hello, say_world)
say_hello()



def inner_func(a, b):
    def add():
        a()  # Викликаємо функцію a
        b()  # Викликаємо функцію b
    return add

def say_hello():
    print('Hello')

def say_world():
    print('World')

# Передаємо дві різні функції у inner_func
say_hello_and_world = inner_func(say_hello, say_world)

# Викликаємо say_hello_and_world, яка викличе обидві функції
say_hello_and_world()
