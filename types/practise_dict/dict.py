my_dict1 = {
    'a': 10,
    'b': 20,
    'c': 30
}


for key in my_dict1:
    print(key)

for key, value in my_dict1.items():
    print(value)

for key, value in my_dict1.items():
    print(key, value)

mydict_key1 = (my_dict1['a'])
mydict_key2 = (my_dict1['b'])

print(mydict_key1)  # 10
print(mydict_key1, mydict_key2)  # 10 20

first_key = list(my_dict1.keys())[0]  # a
second_key = list(my_dict1.keys())[1] # a b
print(first_key, second_key)

print(my_dict1.values())  # dict_values([10, 20, 30])
print(my_dict1.keys())  # dict_keys(['a', 'b', 'c'])

######################################################3

my_dict = {
    'one': 1,
    'two': 3,
    'three': 2
}

print(my_dict.values())
print(my_dict.keys())

one_value = (my_dict['one'])  # 1
two_value = (my_dict['two'])  # 3

print(one_value, two_value)  # 1 3

one_key = list(my_dict.keys())[0]  # one 
two_key = list(my_dict.keys())[1]  # two
print(one_key, two_key)  # one two

for key in my_dict:
    print(key)

for key, value in my_dict.items():
    print(value)

for key, value in my_dict.items():
    print(key, value)

sorted_items = sorted(my_dict.items())  # Виведення пар ключ-значення відсортованими за значенням
for key, value in sorted(my_dict.items()):
    print(key, value)

reversed_dict = list(reversed(my_dict.items()))
for key, value in reversed_dict:
    print(key, value)