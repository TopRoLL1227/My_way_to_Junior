from dataclasses import dataclass
from pprint import pprint


class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f'Thing: {self.__dict__}'


@dataclass
class ThingData:
    name: str
    weight: int
    price: float


text = Thing('Robin', 80, 1000000)
print(text)

textData = ThingData('Robin', 80, 1000000)
print(textData)
pprint(ThingData.__dict__)