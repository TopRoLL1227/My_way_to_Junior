#  Abbreviate a Two Word Name
def abbrev_name(name):
    g = [i[0]for i in name.split(' ')]
    s = '.'.join(g)
    j = s.upper()
    return(j)

print(abbrev_name('Devon Larrat'))

#  Convert number to reversed array of digits
def digitize(n):
    return [int(x) for x in str(n)[::-1]]

print(digitize(23582357))

#  Returning Strings
def greet(name):
    return f'Hello, {name} how are you doing today?'

print(greet('John'))

#  A Needle in the Haystack
def find_needle(haystack):
    return f"found the needle at position {haystack.index('needle')}"

print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))

#  Opposites Attract
def lovefunc( flower1, flower2 ):
    return True if flower1 % 2 == 0 and flower2 % 2 == 1 or flower1 % 2 == 1 and flower2 % 2 == 0 else False

print(lovefunc(1,4))

#  Beginner - Lost Without a Map
def maps(a):
    return [i*2 for i in a]

print(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))