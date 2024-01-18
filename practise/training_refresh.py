def find_needle(haystack):
    return 'found the needle at position ' + str(haystack.index('needle'))

print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))