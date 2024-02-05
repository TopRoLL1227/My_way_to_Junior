class My_class():
    school = '8'
    year = '2013'

setattr(My_class, 'year', '2023')
print(My_class.year)

new_school = My_class()
print(My_class.__dict__)
print(new_school.__dict__)
new_school.x = '88'
print(new_school.x)
print(new_school.__dict__)  # {'x': '88'}

del new_school.x
print(new_school.__dict__)  # {}