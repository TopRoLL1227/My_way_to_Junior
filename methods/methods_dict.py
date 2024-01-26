#  items() метод словарів, повертає послідовність типу dict.items(), послідовність tuple(key, value)
# my_dict_training = {
#     'x': 1,
#     'title': 'test'
# }

# for item in my_dict_training.items():  # 1
#     #print(item)  # ('x', 1), ('title', 'test)
#     key, value = item
#     print(key, value)  # unpacking tuple
#     print(type(my_dict_training.items()))

# for key, value in my_dict_training.items():
#     print(key, value)

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()  # {}

original_dict = {'a': 1, 'b': 2, 'c': 3}
copied_dict = original_dict.copy()

my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('b')  # 2

my_dict = {'a': 1, 'b': 2, 'c': 3}
dict_items = my_dict.items()  # dict_items([('a', 1), ('b', 2), ('c', 3)])

my_dict = {'a': 1, 'b': 2, 'c': 3}
dict_keys = my_dict.keys()  # dict_keys(['a', 'b', 'c'])

my_dict = {'a': 1, 'b': 2, 'c': 3}
dict_values = my_dict.values()  # dict_values([1, 2, 3])

my_dict = {'a': 1, 'b': 2, 'c': 3}
popped_value = my_dict.pop('b')  # popped_value = 2, my_dict = {'a': 1, 'c': 3}

my_dict = {'a': 1, 'b': 2, 'c': 3}
popped_item = my_dict.popitem()  # popped_item = ('c', 3), my_dict = {'a': 1, 'b': 2}

my_dict = {'a': 1, 'b': 2}
my_dict.update({'b': 3, 'c': 4})  # my_dict = {'a': 1, 'b': 3, 'c': 4}

keys = ['a', 'b', 'c']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)  # {'a': 0, 'b': 0, 'c': 0}

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.get('a'))  # 1
print(my_dict.get('d', 'Key not found'))  # Key not found # Вказання значення за замовчуванням