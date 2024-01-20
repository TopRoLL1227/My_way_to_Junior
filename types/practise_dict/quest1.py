def dict_gpt(dict):
    new_dict = {}
    for key, value in dict.items():
        if int(value) % 2 == 0:
            new_dict[key] = value
        else:
            new_dict[key] = None
    return new_dict
    



print(dict_gpt({'apple': 5, 'banana': 10, 'orange': 8, 'grape': 3, 'pear': 6}))

# my_dict = {
#     'apple': 5,
# 'banana': 10, 
# 'orange': 8, 
# 'grape': 3, 
# 'pear': 6
# }

# for key in my_dict:
#     print(key)

# for key, value in my_dict.items():
#     if value in my_dict.items():
#         print(int(value) % 2)
#     else:
#         None