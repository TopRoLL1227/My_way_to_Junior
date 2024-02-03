# my_list = [x for x in collection]
# my_dict = {k: v for k, v in collection}
# my_dict = {x for x in collection}

my_set1 = {x for x in range(1, 5 + 1)}
print(my_set1)
print(type(my_set1))

##########################################################################################
my_set2 = {x for x in [0, 0, 1, 1, 2, 2, 3, 3]}  # {0, 1, 2, 3}
print(my_set2)

# або:

ez_set = set()
for i in [0, 0, 1, 1, 2, 2, 3, 3]:
    ez_set.add(i)

print(ez_set)
###########################################################################################
words_set =  {x for x in ['hi', 'hello', 'hi', 'hello']}  # {'hello', 'hi'}
print(words_set)