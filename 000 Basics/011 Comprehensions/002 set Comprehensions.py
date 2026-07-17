favourite_chai = {'ginger tea', 'masala tea', 'cardamom tea', 'tulsi tea' , 'lemon tea', 'green tea', 'black tea'}

unique={tea for tea in favourite_chai if 'tea' in tea}
print(unique)

recipes={
    "masala tea": ["Boil water", "add tea leaves", "milk", "sugar", "and spices"],
    "ginger tea": ["Boil water", "add tea leaves", "milk", "sugar", "and ginger"],
    "cardamom tea": ["Boil water", "add tea leaves", "milk", "sugar", "and cardamom"],
    "tulsi tea": ["Boil water", "add tulsi leaves", "honey", "and lemon"],
    "lemon tea": ["Boil water", "add tea leaves", "milk", "sugar", "and lemon"],
    "green tea": ["Boil water", "add green tea leaves", "and lemon"],
    "black tea": ["Boil water", "add black tea leaves", "milk", "sugar", "and spices"]
}

unique_spices={spice for recipe in recipes.values() for spice in recipe if 'and' in spice}
print(unique_spices)