def correct(s):
    g = ''
    for x in s:
        if x == "1":
            g = g + 'I'
        elif x == '5':
            g = g + 'S'
        elif x == '0':
            g = g + 'O'
        else:
            g = g + x
    return g
        
print(correct("L0ND0N"))  # Виведе: LOND0N




