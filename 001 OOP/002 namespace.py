class chai:
    origin = "India"
    
print(chai.origin)

chai.is_hot = True
print(chai.is_hot)

# creating object of class chai

masala_tea = chai()
print(masala_tea.origin)
print(masala_tea.is_hot)

masala_tea.origin = "Sri Lanka"
print(masala_tea.origin)