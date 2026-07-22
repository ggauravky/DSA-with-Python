class a:
    label = "a"
    
class b(a):
    label = "b: masala"

class c(a):
    label = "c: herbal"
    
class d(b, c):
    pass

cup=d()
print(cup.label)
print(d.__mro__)