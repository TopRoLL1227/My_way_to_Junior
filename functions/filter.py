#  class filter(object)
#   filter(function or None, iterable) --> filter object
#  Функція filter створює ітератор, що містить тільки ті елементи iterable, для яких function повертає True.

def f(x):
    return x > 10


a = [10, 5, 649, 37, 28, 281, 94, 61, 576, 0]
b = list(filter(f, a))
print(b)  # [649, 37, 28, 281, 94, 61, 576]

l = ['', 14, 0, 5, 'hello', 7952, 192, 471, ' ']
c = list(filter(bool, l))
print(c)  # [10, 5, 649, 37, 28, 281, 94, 61, 576]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_even(num):
    return num % 2 == 0

filtered_numbers = list(filter(is_even, numbers))
print(filtered_numbers)  # [2, 4, 6, 8]


def my_story(x):
    return x

abg = '1Asdfg123raYHDsfd53]'

bl = list(filter(str.isupper, abg))
print(bl)


my_dict = {
    'kiyv': 1000,
    'NY': 800,
    'Kharkiv': 600,
    'Dublin': 400
}

w = 'k'
new_dict = dict(filter(dict.pop, w))
print(new_dict)