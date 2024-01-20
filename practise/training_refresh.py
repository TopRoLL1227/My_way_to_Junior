my_dict = {
    'a': 10,
    'b': 30,
    'c': 20
}

for key in my_dict:
    print(key)

for key, value in my_dict.items():
    print(value)

for key, value in my_dict.items():
    print(key, value)

sorted_items = sorted(my_dict.items())
for key, value in sorted_items:
    print(key, value)
