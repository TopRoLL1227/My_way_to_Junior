from pprint import pprint
# key: value

a = {i: i**2 for i in range(1, 10 + 1)}
print(a)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

b = {}
for i in range(1, 10 + 1):
    b[i] = i**2

print(b)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

c = {i: len(i) for i in ['space', 'back', 'click']}
print(c)  # {'space': 5, 'back': 4, 'click': 5}

data = {
    'Jeff Bezos': '177',
    'eLona mask': '126',
    'berner Arno': '150',
    'Bill Gates': '124'
}

new_data = {key.title(): int(value) for key, value in data.items()}
pprint(new_data)

ddict1 = {}
for key, value in data.items():
    ddict1[key.title()] = ddict1
    print(ddict1)
