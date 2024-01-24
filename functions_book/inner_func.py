# замикання

def say_name(name):
    def say_goodbye():
        print('Who are ' + name + '?')
    return say_goodbye

# print(say_name('you'))  # Замыкания в Python
n = say_name('you')
n2 = say_name('they')
n()
n2()