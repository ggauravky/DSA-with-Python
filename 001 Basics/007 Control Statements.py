"""
CONTROL STATEMENTS IN PYTHON - All Types
=========================================
Control statements control the flow of program execution.
They decide which code runs and when.
"""

# =============================================================================
# 1. IF STATEMENT
# =============================================================================
# Executes code only if condition is True

age = 18
if age >= 18:
    print("You are an adult")
# Output: You are an adult


# =============================================================================
# 2. IF-ELSE STATEMENT
# =============================================================================
# Executes one block if True, another if False

age = 15
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
# Output: You are a minor


# =============================================================================
# 3. IF-ELIF-ELSE STATEMENT
# =============================================================================
# Multiple conditions checked in order

marks = 85
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
# Output: Grade: A


# =============================================================================
# 4. NESTED IF STATEMENTS
# =============================================================================
# If statement inside another if statement

age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")
# Output: You can drive


# =============================================================================
# 5. FOR LOOP
# =============================================================================
# Repeats code for each item in a sequence

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: apple banana cherry

# Loop with range
for i in range(5):
    print(i, end=" ")
print()
# Output: 0 1 2 3 4

# Loop with range (start, stop, step)
for i in range(2, 10, 2):
    print(i, end=" ")
print()
# Output: 2 4 6 8


# =============================================================================
# 6. WHILE LOOP
# =============================================================================
# Repeats code while condition is True

count = 1
while count <= 5:
    print(count, end=" ")
    count += 1
print()
# Output: 1 2 3 4 5


# =============================================================================
# 7. NESTED LOOPS
# =============================================================================
# Loop inside another loop

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print()  # Blank line after each table


# =============================================================================
# 8. BREAK STATEMENT
# =============================================================================
# Exits the loop immediately

for i in range(10):
    if i == 5:
        break  # Stop when i is 5
    print(i, end=" ")
print()
# Output: 0 1 2 3 4

# Breaking out of while loop
count = 0
while True:
    print(count, end=" ")
    count += 1
    if count >= 5:
        break
print()
# Output: 0 1 2 3 4


# =============================================================================
# 9. CONTINUE STATEMENT
# =============================================================================
# Skips current iteration and continues with next

# Skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i, end=" ")
print()
# Output: 1 3 5 7 9


# =============================================================================
# 10. PASS STATEMENT
# =============================================================================
# Does nothing, placeholder for future code


# Empty function
def my_function():
    pass  # Will implement later


# Empty class
class MyClass:
    pass


# Empty if statement
x = 10
if x > 5:
    pass  # TODO: Add logic here


# =============================================================================
# 11. ELSE WITH FOR LOOP
# =============================================================================
# Executes when loop completes normally (not broken)

for i in range(5):
    print(i, end=" ")
else:
    print("\nLoop completed!")
# Output: 0 1 2 3 4
#         Loop completed!

# With break (else won't execute)
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
else:
    print("\nThis won't print")
print()
# Output: 0 1 2


# =============================================================================
# 12. ELSE WITH WHILE LOOP
# =============================================================================
# Executes when while loop condition becomes False

count = 0
while count < 5:
    print(count, end=" ")
    count += 1
else:
    print("\nWhile loop finished!")
# Output: 0 1 2 3 4
#         While loop finished!


# =============================================================================
# 13. MATCH-CASE STATEMENT (Python 3.10+)
# =============================================================================
# Pattern matching - like switch-case in other languages


def check_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:  # Default case
            return "Unknown Status"


print(check_status(200))  # Output: OK
print(check_status(404))  # Output: Not Found
print(check_status(999))  # Output: Unknown Status


# =============================================================================
# 14. MATCH-CASE WITH PATTERNS
# =============================================================================
# Advanced pattern matching


def describe_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"On Y-axis at {y}"
        case (x, 0):
            return f"On X-axis at {x}"
        case (x, y):
            return f"Point at ({x}, {y})"


print(describe_point((0, 0)))  # Output: Origin
print(describe_point((0, 5)))  # Output: On Y-axis at 5
print(describe_point((3, 4)))  # Output: Point at (3, 4)


# =============================================================================
# 15. TERNARY OPERATOR (Conditional Expression)
# =============================================================================
# One-line if-else statement

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

# More examples
x = 10
result = "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(result)  # Output: Positive


# =============================================================================
# 16. LIST COMPREHENSION WITH IF
# =============================================================================
# Create list with conditional filtering

# Get even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10]

# Square of odd numbers
odd_squares = [num**2 for num in numbers if num % 2 != 0]
print(odd_squares)  # Output: [1, 9, 25, 49, 81]


# =============================================================================
# 17. LIST COMPREHENSION WITH IF-ELSE
# =============================================================================
# Transform items based on condition

numbers = [1, 2, 3, 4, 5]
result = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
print(result)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# Double evens, keep odds same
result = [num * 2 if num % 2 == 0 else num for num in numbers]
print(result)  # Output: [1, 4, 3, 8, 5]


# =============================================================================
# 18. DICTIONARY COMPREHENSION WITH IF
# =============================================================================
# Create dictionary with conditions

# Filter dictionary
original = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered = {k: v for k, v in original.items() if v > 2}
print(filtered)  # Output: {'c': 3, 'd': 4}

# Square even numbers only
numbers = [1, 2, 3, 4, 5]
squares = {num: num**2 for num in numbers if num % 2 == 0}
print(squares)  # Output: {2: 4, 4: 16}


# =============================================================================
# 19. SET COMPREHENSION WITH IF
# =============================================================================
# Create set with conditions

numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_evens = {num for num in numbers if num % 2 == 0}
print(unique_evens)  # Output: {2, 4}


# =============================================================================
# 20. GENERATOR EXPRESSION WITH IF
# =============================================================================
# Memory-efficient iteration with conditions

numbers = range(10)
even_gen = (num for num in numbers if num % 2 == 0)
print(list(even_gen))  # Output: [0, 2, 4, 6, 8]


# =============================================================================
# 21. TRY-EXCEPT (Exception Handling)
# =============================================================================
# Handle errors gracefully

try:
    result = 10 / 2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero!")
# Output: Result: 5.0


# =============================================================================
# 22. TRY-EXCEPT-ELSE
# =============================================================================
# Execute code if no exception occurs

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error occurred!")
else:
    print(f"Success! Result: {result}")
# Output: Success! Result: 5.0


# =============================================================================
# 23. TRY-EXCEPT-FINALLY
# =============================================================================
# Always executes finally block, even after errors

try:
    file = open("test.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always executes")
# Output: File not found!
#         This always executes


# =============================================================================
# 24. TRY-EXCEPT-ELSE-FINALLY
# =============================================================================
# Complete exception handling

try:
    num = int("123")
except ValueError:
    print("Invalid number!")
else:
    print(f"Number: {num}")
finally:
    print("Cleanup completed")
# Output: Number: 123
#         Cleanup completed


# =============================================================================
# 25. MULTIPLE EXCEPT BLOCKS
# =============================================================================
# Handle different exceptions differently

try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Index out of range!")
except ValueError:
    print("Value error!")
except Exception as e:  # Catch all other exceptions
    print(f"Some other error: {e}")
# Output: Index out of range!


# =============================================================================
# 26. ASSERT STATEMENT
# =============================================================================
# Check if condition is True, raise error if False

age = 20
assert age >= 18, "Age must be 18 or older"
print("Access granted")
# Output: Access granted

# This would raise AssertionError
# age = 15
# assert age >= 18, "Age must be 18 or older"


# =============================================================================
# 27. WITH STATEMENT (Context Manager)
# =============================================================================
# Automatically handles resource management

# File handling
with open("example.txt", "w") as file:
    file.write("Hello, World!")
# File automatically closed after block


# =============================================================================
# 28. NESTED WITH STATEMENTS
# =============================================================================
# Multiple context managers

with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
    f1.write("File 1")
    f2.write("File 2")


# =============================================================================
# 29. WALRUS OPERATOR WITH IF (Python 3.8+)
# =============================================================================
# Assignment within condition

# Traditional way
data = input("Enter a number (or 'q' to quit): ")
# if data != 'q':
#     print(f"You entered: {data}")

# With walrus operator
# if (data := input("Enter: ")) != 'q':
#     print(f"You entered: {data}")


# =============================================================================
# 30. LOOP WITH ENUMERATE
# =============================================================================
# Loop with index and value

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# Start index from 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")


# =============================================================================
# 31. LOOP WITH ZIP
# =============================================================================
# Loop through multiple lists simultaneously

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")
# Output:
# Alice is 25 years old and lives in New York
# Bob is 30 years old and lives in London
# Charlie is 35 years old and lives in Paris


# =============================================================================
# 32. LOOP WITH REVERSED
# =============================================================================
# Loop in reverse order

numbers = [1, 2, 3, 4, 5]
for num in reversed(numbers):
    print(num, end=" ")
print()
# Output: 5 4 3 2 1


# =============================================================================
# 33. LOOP WITH SORTED
# =============================================================================
# Loop through sorted sequence

numbers = [3, 1, 4, 1, 5, 9, 2]
for num in sorted(numbers):
    print(num, end=" ")
print()
# Output: 1 1 2 3 4 5 9


# =============================================================================
# 34. ANY AND ALL WITH CONDITIONS
# =============================================================================
# Check if any or all items meet condition

numbers = [1, 2, 3, 4, 5]

# any() - True if at least one is True
has_even = any(num % 2 == 0 for num in numbers)
print(f"Has even number: {has_even}")  # Output: True

# all() - True if all are True
all_positive = all(num > 0 for num in numbers)
print(f"All positive: {all_positive}")  # Output: True


# =============================================================================
# 35. FILTER WITH CONDITIONS
# =============================================================================
# Filter items based on condition

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]


# =============================================================================
# 36. MAP WITH CONDITIONS
# =============================================================================
# Transform items conditionally
#definition if map with conditions:  
# Apply function to each item, with conditional logic inside the function 

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2 if x % 2 == 0 else x, numbers))
print(doubled)  # Output: [1, 4, 3, 8, 5]