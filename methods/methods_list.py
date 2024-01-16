my_list = ['apple', 'banana', 'orange', 'grape']  # list.index(element, start, end)
index = my_list.index('orange')
print(f"Индекс слова 'orange': {index}")

my_list = [1, 2, 3]
my_list.append(4)  # [1, 2, 3, 4]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)  # list1 тепер [1, 2, 3, 4, 5, 6]

my_list = [1, 2, 3]
my_list.insert(1, 5)  # [1, 5, 2, 3]

my_list = [1, 2, 3, 2]
my_list.remove(2)  # [1, 3, 2]

my_list = [1, 2, 3]
popped_value = my_list.pop(1)  # popped_value = 2, my_list = [1, 3]

my_list = [1, 2, 3, 2]
index = my_list.index(2)  # index = 1

my_list = [1, 2, 3, 2]
count = my_list.count(2)  # count = 2

my_list = [3, 1, 4, 1, 5, 9, 2]
my_list.sort()  # my_list = [1, 1, 2, 3, 4, 5, 9]

my_list = [1, 2, 3]
my_list.reverse()  # my_list = [3, 2, 1]

my_list = [1, 2, 3]
my_list.clear()  # my_list = []

original_list = [1, 2, 3]
copied_list = original_list.copy()


