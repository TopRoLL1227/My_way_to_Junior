test = 'str'
test1 = ['list']
test2 = {'dict': '1'}
test3 = (1, 2, 3)  # tuple
test4 = {1, 2, 3}   # set

print(type(test))
print(type(test1))
print(type(test2))
print(type(test3))
print(type(test4))


i = ['apple', 'banana', 'lime']
for x in i[0:2]:
    print(' '.join(x).split()[2:4])
    print(type(x))


my_dict_object = {
    'x': 10,
    'y': True,
    'z': 'abc'
}
for key in my_dict_object:  #  key - it is name of  key(x, y, z)
    print(key, my_dict_object[key])


my_dict_1 = { 
    'a': 500,
    'b': True,
    'c': 'abc'
    }

for key in my_dict_1:
    print(key)
    print(my_dict_1[key])

name = 'Sam Harris'
print(type(name))
s = name.split(' ')
print(s)
print(type(s))

# def count_by(x, n):
#     arr = []
#     for num in range(1, n+1):
#         result = x * num
#         arr.append(result)
#     return arr

# def rps(p1, p2):
#     hand = {'rock':0, 'paper':1, 'scissors':2}
#     results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
#     return results[hand[p1] - hand[p2]]


# print(rps('paper', '')) 

number1 = 12345
number_list1 = list(str(number1))  # ['1', '2', '3', '4', '5']

print(number_list1)

number1 = 12345
number_list1 = str(number1)  # error

print(number_list1)