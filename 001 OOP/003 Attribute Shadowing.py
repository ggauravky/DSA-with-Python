class chai:
    temperature = "hot"
    strength = "strong"
    
cutting =chai()
print(cutting.temperature)
print(cutting.strength)

cutting.temperature = "cold"
print(cutting.temperature)

print(chai.temperature)

del cutting.temperature
print(cutting.temperature)