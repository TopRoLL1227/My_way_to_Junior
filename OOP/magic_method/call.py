# class Counter:
#     def __init__(self):
#         self.__counter = 0


# c = Counter() 
#c()  # TypeError: 'Counter' object is not callable # Екземляри класа подібному класу викликати не можна, бо не визначений __call__


###################################


class Counter1:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print("__call__")
        self.__counter += step
        return self.__counter  # Прописаний метод __call__ для екземпляру класу
    

c1 = Counter1()
c2 = Counter1()
c1()  # __call__
c1(4)
res = c1(5)
res2 = c2(-11)
print(res, res2)  # 3 1