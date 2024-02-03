from typing import Union
# Dynamic typing
# Виключно інформаційний характер, на виконання програми ніяким чином не впливає.
# Якщо змінній присвоїти значення, то воно автоматично приймає необхідний тип.
cnt: int = 1

def mul2(x: Union[int, float], y: int | float) -> Union[int, float]:
    return x * y

print(mul2(5, 5.5))
print(mul2.__annotations__)  # {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>} якщо без імпорту Union
print(mul2.__annotations__)  # {'x': typing.Union[int, float], 'y': typing.Union[int, float], 'return': [<class 'int'>, <class 'float'>]}


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

lst: list[int] = [1, 2, 3]

adr: tuple[int, str] = (1, 'asd')
book: tuple(float, ...)
elems = (1,0, 2,0)

words: dict[str, int] = {'one': 1, 'two': 2}

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#def get_positive(digits: list[int]) -> list[int]:  # На вхід подається колекція у виді list з елементами int і повертатиме list з int