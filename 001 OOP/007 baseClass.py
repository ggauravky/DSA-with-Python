class chai:
    def __init__(self, type_ , strength):
        self.type_ = type_
        self.strength = strength

# class gingerchai(chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type_ = type_
#         self.strength = strength
#         self.spice_level = spice_level

# class gingerchai(chai):
#     def __init__(self, type_, strength, spice_level):
#         chai.__init__(self, type_, strength)
#         self.spice_level = spice_level

class gingerchai(chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level

cd=gingerchai("ginger", "strong", "high")
print(cd.type_)
print(cd.strength)
print(cd.spice_level)