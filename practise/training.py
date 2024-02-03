
# my_dict = {
#     'one': 1,
#     'two': 3,
#     'three': 2
# }

# print(my_dict.values())
# print(my_dict.keys())

# one_value = (my_dict['one'])  # 1
# two_value = (my_dict['two'])  # 3

# print(one_value, two_value)  # 1 3

# one_key = list(my_dict.keys())[0]
# two_key = list(my_dict.keys())[1]
# print(one_key, two_key)


def local(b):
    global a  # Використовуємо global, оскільки a - глобальна змінна
    a = 10
    b.append(80)
    return a, b

a = 1000
result = local([])
print(result)


