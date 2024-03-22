# # string = '***Vovik, vovik***'
# # new_string = string.strip('*')
# # print(new_string)  # 'Vovik, vovik'


# def my_func(chars):
#     def my_func1(string):
#         print(string.strip(chars))
#     return my_func1

# asd = my_func('***')
# asd('***Vovik, vovik***')


def to_jaden_case(string):
    list = string.split(' ')
    new_list = [i.capitalize() for i in list]
    return ' '.join(new_list)
    

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))


"People Tell Me To Smile I Tell Them The Lack Of Emotion In My Face Doesn'T Mean I'M Unhappy"
"People Tell Me To Smile I Tell Them The Lack Of Emotion In My Face Doesn't Mean I'm Unhappy"


asd = lambda a, b: a * b

print(asd(1, 2))
