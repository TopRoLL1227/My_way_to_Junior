# ZIP
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