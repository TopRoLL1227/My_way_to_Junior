def dict_gpt(dict):
    new_dict = {}
    for key, value in dict.items():
        if int(value) % 2 == 0:
            new_dict[key] = value
        else:
            new_dict[key] = None
    return new_dict
    



print(dict_gpt({'apple': 5, 'banana': 10, 'orange': 8, 'grape': 3, 'pear': 6}))