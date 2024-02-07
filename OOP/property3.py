from string import ascii_letters

class Person:
    s_ENG = 'abcdefghjklmnopqrstuvwxyz-'
    S_ENG_UPPER = s_ENG.upper()
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.__fio = fio.split()
        self.__old = old
        self.__ps = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("FIO need to be sting")
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Don't correct format")
        
        letters = ascii_letters + cls.s_ENG + cls.S_ENG_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('Need more than 1 symbol')
            if len(s.strip(letters)) != 0:
                raise TypeError('Fio need to be used only words or hyphen')
            
p = Person('Jackson Jack Jackky', 30, '123456', 80.0)
