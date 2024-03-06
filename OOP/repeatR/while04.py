# i = 1
# while 5 > 1:  # while True
#     print('Iteration nomer', i)
#     if i == 10:
#         break
#         print('Hi')
#     i = i + 1
# print('hello')

################# break
# while True:
#     a = input()
#     if a == 'exit':
#         break
#     print(a, len(a))


################# continue
# while True:
#     a = input()
#     if a == 'exit':
#         break  
#     if len(a) < 5:
#         continue  # перекидує на початок циклу
#     print(a, len(a))

################ else
# i = 1
# while i <= 15:
#     print(i)
#     i = i + 1
# else:             # буде виконуватися тоді, коли цикл завершиться сам по собі
#     print('good')
#     print('job')
# print('end')

a = [7, 48, 32, 678, 26]
while len(a) > 0:
    last = a.pop()
    if last % 2 != 0:
        print('No', a)
        break
else:
    print("Yes")