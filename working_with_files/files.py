file = open('111.txt', encoding = 'utf-8')  # кодування для кирилиці
print(file.read())

file1 = open(r'/home/volodymyr/git/My_way_to_Junior/working_with_files/222.txt')
print(file1.read())

#  У Python префікс r перед рядком вказує на "сирі" (raw) рядки. 
#  Коли ви використовуєте префікс r перед рядком, він вказує інтерпретатору Python ігнорувати будь-які спеціальні символи у рядку.

file1 = open(r'/home/volodymyr/git/My_way_to_Junior/working_with_files/222.txt')
print(file1.read(2))  # Роздрукує два символи: Do
print(file1.read(2))  # Роздрукує наступні два символи від попередніх: h

file1.seek(0)  # У вашому випадку file.seek(0) використовується для переміщення вказівника файлу на початок файлу (зміщення 0). 
              # Це означає, що якщо ви раніше читали чи записували в файл, наступна операція розпочнеться з початку.
print(file1.read(2))  # Після seek(0) вернуло вказівник на початок

file1.seek(0)

print(file1.readline())  # зчитує перший рядок 
print(file1.readline())  # зчитує другий рядок


#################################################################################################################

file333 = open(r'/home/volodymyr/git/My_way_to_Junior/333.txt', 'w')  #  У цьому прикладі 'w' вказує, що файл 333.txt буде відкритий для запису. 
                                                                      #  Якщо файл існує, його вміст буде видалено, і файл буде готовий для нового запису. 
                                                                      #  Якщо файл не існує, він буде створений.
file333.write('hello\n')
file333.write('hello\n')
file333.write('hello')


file333 = open(r'/home/volodymyr/git/My_way_to_Junior/333.txt', 'a')  # Дописує, а не перезаписує. 
file333.write('\nVovik')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'a' лише write,не  read!!!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'a+' одночасно за запис й зчитування!!!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

file333.close()  # Обов'язковий параметр!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!