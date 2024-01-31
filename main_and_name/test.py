def my_f():
    print(f'this is TEST.py>>>>>>{__name__}')

def hello():
    print(f'This is MAIN_TEST2.PY>>>>>>>>>{__name__}')


if __name__ == '__main__':
    my_f()
else:
    hello()