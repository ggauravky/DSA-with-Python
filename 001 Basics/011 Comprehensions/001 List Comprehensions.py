menu=[
    "Pasta",
    "Pizza",
    "Salad",
    "Soup"
]

# List Comprehension
menu_items = [item for item in menu if len(item) > 4]
print(menu_items)

# some more examples of list comprehensions

list1 = [1, 2, 3, 4, 5]
# Squaring each number in the list
squared_list = [num ** 2 for num in list1]
print(squared_list)

# Filtering even numbers from the list
even_numbers = [num for num in list1 if num % 2 == 0]
print(even_numbers)

# Creating a list of tuples with number and its square
number_square_tuples = [(num, num ** 2) for num in list1]
print(number_square_tuples)

# Creating a list of strings with a prefix
prefix = "Item: "
prefixed_items = [prefix + item for item in menu]
print(prefixed_items)

# Creating a list of lengths of each item in the menu
item_lengths = [len(item) for item in menu]
print(item_lengths)