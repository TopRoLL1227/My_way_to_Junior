class Lion:

    def __init__(self, name):
        self.name = name


q = Lion('Bob')
print(q)  # 0x7f8f21716ef0>
print(str(q))  # 0x7f8f21716ef0>


print("#####################################################################")
##############################################################################

class Lion1:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"The object Lion - {self.name}"

a = Lion1('Simba')
print(a)




print("#####################################################################")
##############################################################################

class Lion2:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"The object Lion - {self.name}"
    
    def __str__(self):
        return f"Lion - {self.name}"


e = Lion2('Eddy')
print(e)
print(str(e))