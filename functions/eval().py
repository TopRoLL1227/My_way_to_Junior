# eval() приймає один обов'язковий аргумент рядок
source = '5 + 5'
print(source) 

result = eval(source)
print(result)  # 10
eval('print(5 * 5)')  # 25

# def basic_op(operator, value1, value2):
#     return eval(f'{value1}{operator}{value2}')

# print(basic_op('*', 4, 7))