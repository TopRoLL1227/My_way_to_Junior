import mypackage.file1
import mypackage.file2



print(mypackage.file1.b)
print(mypackage.file2.d)

# або:

from mypackage import file1 as f1
from mypackage import file2 as f2

print(f1.b)
print(f2.d)

# або:

from mypackage.file1 import a

print(a)

mypackage.a  # 10 -----------> див. file1 --------------> після див. __init.py 
# mypackage.c  # Error, бо в модулі file1 використаний __all__ який вказує на те, що може бути імпортоване. Якщо я хочу імпортувати опосередковано, потрібно
             # викликати mypackage.file1.c. Якщо хочу, щоб зчитував всі модулі потрібно "налаштувати" у файлі __init__.py
             # Файл __init__.py зчитує і передає цю інформацію сюди.
