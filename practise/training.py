# string = '***Vovik, vovik***'
# new_string = string.strip('*')
# print(new_string)  # 'Vovik, vovik'


def my_func(chars):
    def my_func1(string):
        print(string.strip(chars))
    return my_func1

asd = my_func('***')
asd('***Vovik, vovik***')