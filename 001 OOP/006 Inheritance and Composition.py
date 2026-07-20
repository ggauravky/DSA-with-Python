class basechai:
    def __init__(self, name):
        self.name = name

    def prepare(self):
        print(f"Preparing {self.name} base chai.")

class masalachai(basechai):
    def add_spices(self):
        print(f"Adding spices to {self.name} masala chai.")

class chaishop:
    chai_cls=basechai
    
    def __init__(self):
        self.chai = self.chai_cls("Regular")
        
    def serve_chai(self):
        print(f"Serving {self.chai.name} chai.")
        self.chai.prepare()
        
class fancychaishop(chaishop):
    chai_cls=masalachai
    
shop=chaishop()
fancy_shop=fancychaishop()
fancy_shop.serve_chai()
fancy_shop.chai.add_spices()
fancy_shop.chai.prepare()