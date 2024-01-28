# Функція enumerate() в Python використовується для отримання ітератора, який повертає пари індексу та відповідного елемента з визначеного об'єкта 
# (списку, кортежу, рядка тощо). Це дозволяє одночасно пройти по індексам та елементам об'єкта.

fruits = ['apple', 'banana', 'lemon']

for index, value in enumerate(fruits):
    print(f'index: {index}, value: {value}')  # index: 0, value: apple
                                              # index: 1, value: banana
                                              # index: 2, value: lemon
    
for para in enumerate(fruits):  # 6 пар
    print(para)  # (0, 'apple')
                 # (1, 'banana')
                 # (2, 'lemon')
    
for index, value in enumerate(fruits):
    print(index, value)  # 0 apple
                         # 1 banana
                         # 2 lemon

string = 'abcdef' 

for index, value in enumerate(string):
    print(index, value)

for index, value in enumerate(range(10, 20, 2)):
    print(index, value)  # 0 10
                         # 1 12
                         # 2 14
                         # 3 16
                         # 4 18