# Example

# Ітеруємим об'єктом є list
s = [1, 2, 3]
# next(s) # TypeError: 'list' object is not an iterator

d = iter(s) # З ітеруючого об'єкту получаємо ітератор за допомогою iter()  
print(next(d))  # 1
print(next(d))  # 2
print(next(d))  # 3
#print(next(d))  # StopIteration
#Ітератора зберігає інформацію який елемент буде наступним.

# Від самого початку генератор є ітератором
generator_expression = (x**2 for x in range(10))
print(generator_expression)  # <generator object <genexpr> at 0x7f1cd6b42570>
print(next(generator_expression))  # 0
print(next(generator_expression))  # 1
print(next(generator_expression))  # 2

list_comprehension = [x**2 for x in range(10)]
print(list_comprehension)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#print(next(list_comprehension))  # 'list' object is not an iterator

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>ГЕНЕРАТОР - ітератор, елементи якого можна ітерувати лише один раз!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Під ітерацією розуміється процес перебору елементів колеціїї всередині циклу або якоїсь функції
# Example:
generator_expression = (x**2 for x in range(10))
for i in generator_expression:
    print(i)

for i in generator_expression:
    print(i)  #>>>>>>>>>>>>>>>>>>>>>>>>> Другий раз нічого не вийде тому, що ітератор підтримує один обхід
# Це відбувається тому, що елементи генаратора не зберігаються у пам'яті всі разом, а створюються на льоту. Це плюс генератора.


list_comprehension = [x**2 for x in range(10)]
print(list_comprehension)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(list_comprehension)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

i= [x**2 for x in range(6)]
print(i)
#c = list(range(10000000000))  # MemoryError
#c = [i for i in range(10000000000)]  # MemoryError
#c = (i for i in range(100000000)) 
#for i in c:
#    print(i) # Поїхали


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Обмеження та різниця<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
g = [x**2 for x in range(1, 6)]
print(g)  # [1, 4, 9, 16, 25]
k = (x**2 for x in range(1, 6))
print(k)  # <generator object <genexpr> at 0x7fcfa2726500>
print(list(k)) [1, 4, 9, 16, 25]

print(len(g))
