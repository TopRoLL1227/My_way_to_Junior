import os

with os.scandir('.') as entry:
    for i in entry:
        print(i.name)