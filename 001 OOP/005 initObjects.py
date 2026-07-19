class chai:
    def __init__(self,type_, size):
        self.type = type_
        self.size = size
        
    def summary(self):
        return f"This is a {self.size}ml cup of {self.type} chai."
    

order= chai("Masala", 200)
print(order.summary())


order2= chai("Ginger", 250)
print(order2.summary())