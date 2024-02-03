import os
# Контекстні менеджери реалізують два методи: __enter__ та __exit__. Метод __enter__ викликається при вході в блок with, 
# а метод __exit__ викликається при виході з блоку, навіть у випадку виникнення виключення.

#file1 = open(r'/home/volodymyr/git/My_way_to_Junior/meneger_context/test.txt', 'w')
#file1.write([1, 2, 3])  # write() argument must be str, not list
#file1.close()  # не спрацює, бо error при записі

#lst = []
#for i in range(10000):  # [Errno 24] Too many open files: '/home/volodymyr/git/My_way_to_Junior/meneger_context/test.txt'
#    lst.append(open(r'/home/volodymyr/git/My_way_to_Junior/meneger_context/test.txt', 'w'))

# Помилка [Errno 24] каже, що зовнішній ресурс до якого йде підключення має ресурс по підключенню, до нього неможливо підключитися багато разів
# Вихід з ситуації:
    
#lst = []
#for i in range(10000):  # Після закриття файлу проблема не виникає
#    file = open(r'/home/volodymyr/git/My_way_to_Junior/meneger_context/test.txt', 'w')
#    lst.append(file)
#    file.close()

# Менеджер контексту with гарантує закриття файлу незалежно від того, були помилки чи ні.
    
with open(r'/home/volodymyr/git/My_way_to_Junior/meneger_context/test.txt', 'w') as f:  # відкриє файл в режимі читання
    f.write('123')
    f.write('Hello')

print('end')  # Між 25 та 26 автоматично викликається метод close() 


with os.scandir(".") as entries:
    for entry in entries:
        print(entry.name, "->", entry.stat().st_size, "bytes")