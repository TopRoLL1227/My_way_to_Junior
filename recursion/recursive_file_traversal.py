#  Рекурсивний обхід файлів
import os 

# path = '/home/volodymyr/test'

# print(os.listdir(path))  # ['Untitled3.odt', 'Untitled2.odt', 'Untitled1.odt']
# for i in (os.listdir(path)):
#     print(i, type(i))  # str
#     print(path + '/' + i)  # виводить шлях файлу
#     print(os.path.isdir(path + '/' + i))  # перевіряє, чи даний елемент є папкою, або ні
#     print(os.path.isfile(path + '/' + i))  # перевіряє, чи даний елемент є файлом, або ні





########################################################################
    
path = '/home/volodymyr/'

def obxodFile(path, level=1):
    print('Level=', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '/' + i):
            print('Спускаємось', path + '/' + i)
            obxodFile(path + '/' + i, level + 1)
            print('Вертаємось в', path)
obxodFile(path)