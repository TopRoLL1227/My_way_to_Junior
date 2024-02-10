# dunder - double underscore
# Ці методи спрацьовують в момент відображення інформації про об'єкт класа. 

class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f'The object  Lion - {self.name}'

    def __str__(self) -> str:
       return f'Lion - {self.name}'

asd = Lion('Cayse')
print(asd)  # <__main__.Lion object at 0x7f02fa556d40>
print(asd)  #  Після створення методу __repr__ вивід буде: The object  Lion - Cayse

print(asd())

