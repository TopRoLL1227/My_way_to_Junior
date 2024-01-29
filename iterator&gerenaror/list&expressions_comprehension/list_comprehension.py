# # Генератор списків
# a = 1, 2
# print([eval('x*x') for x  in a])

# s = [(x,z) for x in 'abc' for z in [1, 2, 3]]
# print(s)  # s = [(x,z) for x in 'abc' for z in [1, 2, 3]]

# numb = [j*i for j in [1, 2, 3, 4, 5] for i in [1, 2, 3] if j*i > 10]
# print(numb) # [12, 15]


a = [
    ('Shevchenko', 1814),
    ('Kostenko', 1930),
    ('Bandera', 1909),
    ('Vernadskiy', 1863),
    ('Pushkar', 1985),
    ('Usyk', 1987)
]

b = [x[0] for x in a]
print(b)  # ['Shevchenko', 'Kostenko', 'Bandera', 'Vernadskiy']

n = [x[0] for x in a if x[1] > 1980]
print(n)

c = [x[0][0] for x in a]
print(c)  # ['S', 'K', 'B', 'V', 'P', 'U'] Звертаюся до індексу в індексі.

asd = [1, 2, 3]
b = [(i, j) for i in asd for j in 'asd']
print(b)


my_dict = {
    'Shevchenko': {'age': 1814, 'hobby': 'poet'},
    'Kostenko': {'age': 1930, 'hobby': 'writer'},
    'Bandera': {'age' : 1909, 'hobby': 'political'},
    'Vernadskiy': {'age': 1863, 'hobby': 'scientist'},
    'Pushkar': {'age': 1985, 'hobby': 'arm'},
    'Usyk': {'age': 1987, 'hobby': 'box'}
}

d = [(x, my_dict[x]['age']) for x in my_dict]
print(d)