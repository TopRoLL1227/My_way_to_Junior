#  items() метод словарів, повертає послідовність типу dict.items(), послідовність tuple(key, value)
my_dict_training = {
    'x': 1,
    'title': 'test'
}

for item in my_dict_training.items():  # 1
    #print(item)  # ('x', 1), ('title', 'test)
    key, value = item
    print(key, value)  # unpacking tuple
    print(type(my_dict_training.items()))

for key, value in my_dict_training.items():
    print(key, value)


