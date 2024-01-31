import pprint
import calendar
import math as m
# Модуль це будь-яка програма створена у форматі .py
# Окрім імені у модуля є ще два головних атрубита: 1) Його місцезнаходження, 2) Простір імен

# https://docs.python.org/3/py-modindex.html#cap-c


def say_hello(name):
    print(f'Hello, {name}')

def summa(*args):
    return sum(*args)

def factorial(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr

my_str = "Playmaker"
my_num1 = 2
my_num2 = 3

# c = calendar.TextCalendar()
# print(c.formatyear(2020))

print(m.pi)

