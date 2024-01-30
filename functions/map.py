# class map(object)
#   map(func, *iterables) --> map object

def f(x):
    return x**2


a = [-1, 2, -3, 4, 5]
b = list(map(f, a))
print(b)  # [1, 4, 9, 16, 25]


n = ['hello', 'hi', 'good morning']
l = list(map(len, n))
print(l)  # [5, 2, 12]


n = ['hello', 'hi', 'good morning']
l = list(map(str.upper, n))
print(l)  # ['HELLO', 'HI', 'GOOD MORNING']

s = list(map(int, input().split()))
print(s)
