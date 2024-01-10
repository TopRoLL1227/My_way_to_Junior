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