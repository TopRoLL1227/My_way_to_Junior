baza = {
    'name': 'Vova',
    'is_student': True
} 
info_baza = baza

print(id(baza))
print(id(info_baza))
info_baza1 = baza.copy()
print(id(info_baza1))
