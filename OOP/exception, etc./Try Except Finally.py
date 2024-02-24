# обробка винятків

try:
    int('123')
    print('1, 2, 3')
    a + b
except ValueError:
    print('NameError')
except ZeroDivisionError:
    print('ZeroDivisionError:')
except NameError:
    print('NameError')


print('#' * 70)
#######################################################################

s = 'hello'
d = {}
try:
    d['key']
except ValueError:
    print('NameError')
except ZeroDivisionError:
    print('ZeroDivisionError:')
except NameError:
    print('NameError')
except LookupError:
    print('IndexError')

print('#' * 70)
#######################################################################

s = 'hello'
d = {}
try:
    4+'asd'
except:
    print('All error')

print('#' * 70)
#######################################################################

s = 'hello'
d = {}
try:
    4+8
except Exception:
    print('All error')
finally:  # буде виконуватися завжди, незалежно від того, чи було здійснено виключення у блоці Exception
    print('end')

# except може бути багато разів, finally лише один раз
    

print('#' * 70)
#######################################################################

s = 'hello'
d = {}
#f = open('123.txt')
try:
    1/5
except (KeyError, IndexError):
    print(LookupError)
except ZeroDivisionError:
    print('ZeroDivisionError')  
else:              # виконається у тому випадку, коли в try немає виключення
    print('good')
finally:  
    print('end')
    #f.close()
