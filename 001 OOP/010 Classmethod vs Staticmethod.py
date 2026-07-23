class chaiorders:
    def __init__(self, tea_type,sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
    
    @classmethod
    def from_dict(cls,order_dict):
        return cls(order_dict['tea_type'], order_dict['sweetness'], order_dict['size'])

    @classmethod
    def from_string(cls,order_string):
        tea_type, sweetness, size = order_string.split('-')
        return cls(tea_type, sweetness, size)
    
class chaiUtils:
    @staticmethod
    def is_valid_order(size):
        return size in ['Small', 'Medium', 'Large']
    
print(chaiUtils.is_valid_order('Medium'))
    
order1 = chaiorders.from_dict({'tea_type':'Masala Chai', 'sweetness':'Medium', 'size':'Large'})
order2 = chaiorders.from_string('Green Tea-Low-Small')

print(order1.__dict__)
print(order1.tea_type, order1.sweetness, order1.size)
print(order2.__dict__)
print(order2.tea_type, order2.sweetness, order2.size)