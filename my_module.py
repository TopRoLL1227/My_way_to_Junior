#import moduls.dir.import_st_library
from moduls.dir.import_st_library import my_num1, my_str
from moduls.dir.import_st_library import factorial
import sys
import pprint

print(factorial(10))

print(my_num1)
print(my_str)

# Що відбувається хайлевелно?
# Три операції
# 1. Python шукає файл(імпорт) за допомогою:
#    import.sys
#    sys.path 
pprint.pprint(sys.path)

# Пайтон знайшовши модуль перетворює його в byte code