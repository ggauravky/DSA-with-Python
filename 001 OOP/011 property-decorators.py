class TeaLeaf:
    def __init__(self,age):
        self.age = age
    
    @property
    def age(self):
        return self._age+2
    
    @age.setter
    def age(self,age):
        if 1<age<10:
            self._age = age
        else:
            raise ValueError('Age must be between 1 and 10')

leaf1 = TeaLeaf(5)
print(leaf1.age)

leaf1.age = 9
print(leaf1.age)