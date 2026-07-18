class chaicup:
    size = 150
    
    def describe(self):
        return f"This chaicup is {self.size}ml in size."
    
cup=chaicup()
print(cup.describe())
#print(chaicup.describe) #error-> this is because describe() is an instance method and needs an instance to be called.  

