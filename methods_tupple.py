# Маючи на увазі кортежі (tuples) в Python, важливо зауважити, що кортежі є немутабельними послідовностями, 
# тобто їх не можна змінювати після створення. Ось кілька основних методів для роботи з кортежами:

my_tuple = (1, 2, 2, 3, 4, 2)
count_of_2 = my_tuple.count(2)  # 3

my_tuple = (1, 2, 3, 4, 5)
index_of_3 = my_tuple.index(3)  # 2

my_tuple = (1, 2, 3, 4, 5)
length_of_tuple = len(my_tuple)  # 5

my_tuple = (3, 1, 4, 1, 5, 9, 2)
sorted_tuple = tuple(sorted(my_tuple))  # (1, 1, 2, 3, 4, 5, 9)

my_tuple = (True, False, True, True)
any_result = any(my_tuple)  # True (хоча б один True)
all_result = all(my_tuple)  # False (не всі True)
