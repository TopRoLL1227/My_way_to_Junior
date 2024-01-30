file = open('111.txt', encoding = 'utf-8')  # кодування для кирилиці
print(file.read())

file1 = open(r'/home/volodymyr/git/My_way_to_Junior/working_with_files/222.txt')
print(file1.read())

#  У Python префікс r перед рядком вказує на "сирі" (raw) рядки. 
#  Коли ви використовуєте префікс r перед рядком, він вказує інтерпретатору Python ігнорувати будь-які спеціальні символи у рядку.