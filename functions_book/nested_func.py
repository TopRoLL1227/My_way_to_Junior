# Вкладена функція - це функція, яка визначається всередині іншої функції. 
# Така вкладеність означає, що внутрішня функція має доступ до змінних і параметрів зовнішньої функції

g = 'grey'


def colors():
    
    y = 'yellow' 

    def print_red():
        nonlocal y  # застосовується лише тоді, коли можна посилатися на локальні змінні
        r = 'red'
        print(r, y, g)  # red yellow grey
        y = 'was changed'
        #print(r, b)  # Error


    def print_blue():
        b = 'blue'
        print(b, y, g)  # blue was chanched grey. Чому was changed? y = 'yellow' змінили на 'was changed' рядком nonlocal y

    print_red()
    print_blue()


    # if param == 'r':
    #     print_red()
    # elif param =='b':
    #     print_blue()
    # else:
    #     print('I do know this color')

colors()
#print_red()  # Error


def f1(a):
    
    def f2(b):
        print(a * b)

    def f3(c):
        print(a / c)

    return f2, f3


f2, f3 = f1(10)

f1(f2(2))  # 20
f1(f3(5))  # 2.0