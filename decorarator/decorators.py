# декоратор це функція яка розширює функціонал іншої функції

def decorator(func):
    def inner():
        print('start decorator...')
        func()
        print('finish decorator')
    return inner


def say():
    print('hello world')

d = decorator(say)
t = decorator(say)
#print(d)  # <function decorator.<locals>.inner at 0x7f214a386d40>
d() 
t()


# Як при виклику функції say одночасно викликати функцію def decorator?
# Декоратор це функція яка приймає іншу функцію і повертає функцію. Декоратор потрібен для того, щоб у функції з'явився новий функціонал(поведінка)
def decorator1(func):
    def inner1(n):
        print('start decorator...')
        func(n)
        print('finish decorator')
    return inner1


def say1(name):
    print('hello world', name)

def buy():
    print('buy world')

say1 = decorator1(say1)
say1('Vovik')  # посилання зберігається не на функцію say, а на функцію inner1
#print(say1)  # <function decorator.<locals>.inner at 0x7fa4d5f2b010>

#buy = decorator(buy)
#buy()  
 

def decorator(close):
        def closure(*args):
            n = args[0]
            print(f'Dyadko {n}, vse byde dubri, golovne vchisya')
            close(*args)
            print(f'Ya v tobi ne symnivausya')
        return closure

def practise(n, h):
    print(f'Training every day {n}, {h}')

practise = decorator(practise)
practise('Vovik', "=D")


def my_func(func):
    def ny_func(*args):
        print("Hello, world")
        res = func(*args)
        print("Happy day!")
        return res
    return ny_func

def test(a):
    print('Yeap')
    return test

test = my_func(test)
test('a')

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def decorator(func):
    def wrapper():
        result = func()
        return f'Result: {result}'
    
    return wrapper


@decorator  # посилання на 1 рядок, decorator()
def dec():
    return 'Hello'

# dec = decorator(dec)
print(dec())


####################################

def decorator(is_raw_return: bool):                        
    def decorator_2(func):
        def wrapper():
            result = func()
            if is_raw_return:
                return result
            return f'Result: {result}'
    
        return wrapper
    return decorator_2


@decorator(is_raw_return = True)  # Викликає функцію decorator() яка створить в собі decorator_2 ..... Тут декорація йде не за допомогою функції decorator(), а декорується 
def dec():    # за допомогою функції яка знаходиться в середині, тобто decorator_2. Тим самим можна використовувати аргументи в decorator(). Див decorator()
    return 'Hello'

# dec = decorator(dec)
print(dec())

#######################

def decorator(practise):
    def multiplay(*args, **kwargs):
        print(f'Result is: {args}, {kwargs}')
        res = practise(*args, **kwargs)
        print(f'There is {practise.__name__}')
        return res
    return multiplay
    

@decorator
def mathematic(a, b):
    return a * b

@decorator
def school(a, b):
    return a + b

print(school(a = 5, b = 5))
print(mathematic(2, 5))



