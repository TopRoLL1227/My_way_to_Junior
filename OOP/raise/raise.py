# Існтрукція raise

print('hello1')
print('hello2')
print('hello3')
e = ZeroDivisionError('NOPE')
#raise ZeroDivisionError('NOPE')                        # ZeroDivisionError: NOPE
#raise e # так само як raise ZeroDivisionError('NOPE')  # ZeroDivisionError: NOPE
raise 'ZeroDev'                                         # TypeError: exceptions must derive from BaseException
print('hello4')
print('hello5')
print('hello6')


