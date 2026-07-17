# ==================== INPUT METHODS ====================

# 1. Basic input - takes input as string
name = input("Enter your name: ")

# 2. Taking integer input - convert string to int
age = int(input("Enter your age: "))

# 3. Taking float input - convert string to float
height = float(input("Enter your height: "))

# 4. Taking multiple inputs in one line - splits by space
a, b, c = input("Enter three numbers: ").split()

# 5. Taking multiple integers in one line
x, y = map(int, input("Enter two numbers: ").split())

# 6. Taking list of integers
numbers = list(map(int, input("Enter numbers: ").split()))


# ==================== OUTPUT METHODS ====================

# 1. Basic print - prints text
print("Hello World")

# 2. Print variable
print(name)

# 3. Print multiple items - separated by space
print("Name:", name, "Age:", age)

# 4. Print without newline - use end parameter
print("Hello", end=" ")
print("World")

# 5. Print with custom separator - use sep parameter
print("A", "B", "C", sep="-")

# 6. f-string formatting - modern and easy way
print(f"My name is {name} and I am {age} years old")

# 7. format() method - another way to format
print("My name is {} and I am {} years old".format(name, age))

# 8. % formatting - old style
print("My name is %s and I am %d years old" % (name, age))

# 9. Print with precision for floats
pi = 3.14159
print(f"Pi value: {pi:.2f}")  # prints 2 decimal places

# 10. Print special characters
print("Line 1\nLine 2")  # \n for newline
print("Tab\tSpace")  # \t for tab
