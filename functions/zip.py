# zip(iter1 [,iter2 [...]]) --> zip object
# ZIP  - це вбудована функція мови програмування Python, яка об'єднує елементи з двох чи більше ітерабельних об'єктів (списків, кортежів і т. д.). 
# Вона створює новий ітератор, який генерує кортежі, складені з відповідних елементів вихідних ітерабельних об'єктів.
fruits = ['apple', 'banana', 'lime']
quantities = [100, 70, 50]
fruits_qtys_zip = zip(fruits, quantities)

print(fruits_qtys_zip)  # <zip object at 0x7fc6e054cf80>

print(type(fruits_qtys_zip))  # <class 'zip'>

fruits_qtys_zip = list(fruits_qtys_zip)

print(fruits_qtys_zip)  # [('apple', 100), ('banana', 70), ('lime', 50)]

fruits_qtys_zip = dict(fruits_qtys_zip)  # {'apple': 100, 'banana': 70, 'lime': 50}

print(fruits_qtys_zip)  # {'apple': 100, 'banana': 70, 'lime': 50}

availability = [True, False, True]
fruits_qtys_zip = zip(fruits, quantities, availability)
print(list(fruits_qtys_zip))  # [('apple', 100, True), ('banana', 70, False), ('lime', 50, True)]
print(dict(fruits_qtys_zip))  # {}


a = [5, 6, 7, 8]
b = [100, 200, 300, 400]

for i in range(4):
    print(a[i], b[i])

g = [5, 6, 7,]
j = [100, 200, 300, 400]

print(list(zip(g, j)))  # [(5, 100), (6, 200), (7, 300)]


my_string = 'abcd'
my_array = [1, 2, 3, 4]
my_tupple = (5, 6, 7, 8)

for i in zip(my_string, my_array, my_tupple):
    print(i)  # ('a', 1, 5)
              # ('b', 2, 6)
              # ('c', 3, 7)
              # ('d', 4, 8)
    
for t1, t2, t3 in zip(my_string, my_array, my_tupple):
    print(t1, t2, t3)  # a 1 5
                       # b 2 6
                       # c 3 7
                       # d 4 8
    
rez = zip(my_string, my_array, my_tupple)
col1, col2, col3 = zip(*rez)
print(col1, col2, col3)  # ('a', 'b', 'c', 'd') (1, 2, 3, 4) (5, 6, 7, 8)