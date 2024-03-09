class Lion:
 
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"The object Lion - {self.name}"
    
    def __str__(self):
        return f"Lion - {self.name}"

q = Lion('Simba')
print(q)


