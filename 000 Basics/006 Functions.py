"""
FUNCTIONS IN PYTHON - All Types
================================
A function is a reusable block of code that performs a specific task.
"""

# =============================================================================
# 1. BASIC FUNCTION (Simple Function)
# =============================================================================
# Function with no parameters and no return value
# Just executes some code when called


def greet():
    print("Hello, World!")


greet()  # Output: Hello, World!


# =============================================================================
# 2. FUNCTION WITH PARAMETERS
# =============================================================================
# Function that accepts input values (parameters)


def greet_person(name):
    print(f"Hello, {name}!")


greet_person("Alice")  # Output: Hello, Alice!


# =============================================================================
# 3. FUNCTION WITH RETURN VALUE
# =============================================================================
# Function that returns a result back to the caller


def add(a, b):
    return a + b


result = add(5, 3)
print(result)  # Output: 8


# =============================================================================
# 4. FUNCTION WITH DEFAULT PARAMETERS
# =============================================================================
# Parameters that have default values if not provided


def greet_with_time(name, time="morning"):
    print(f"Good {time}, {name}!")


greet_with_time("Bob")  # Output: Good morning, Bob!
greet_with_time("Bob", "evening")  # Output: Good evening, Bob!


# =============================================================================
# 5. FUNCTION WITH KEYWORD ARGUMENTS
# =============================================================================
# Calling function by specifying parameter names


def introduce(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")


introduce(age=25, city="New York", name="John")  # Order doesn't matter


# =============================================================================
# 6. FUNCTION WITH *args (Variable Length Arguments)
# =============================================================================
# Accepts any number of positional arguments as a tuple


def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(1, 2, 3, 4, 5))  # Output: 15


# =============================================================================
# 7. FUNCTION WITH **kwargs (Keyword Variable Arguments)
# =============================================================================
# Accepts any number of keyword arguments as a dictionary


def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


print_info(name="Alice", age=30, job="Engineer")
# Output:
# name: Alice
# age: 30
# job: Engineer


# =============================================================================
# 8. LAMBDA FUNCTION (Anonymous Function)
# =============================================================================
# Small one-line function without a name
# Syntax: lambda arguments: expression

square = lambda x: x**2
print(square(5))  # Output: 25

add = lambda a, b: a + b
print(add(3, 4))  # Output: 7


# =============================================================================
# 9. RECURSIVE FUNCTION
# =============================================================================
# Function that calls itself


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))  # Output: 120


# =============================================================================
# 10. NESTED FUNCTION (Function Inside Function)
# =============================================================================
# Function defined inside another function


def outer_function(text):
    def inner_function():
        print(text)

    inner_function()


outer_function("Hello from inside!")  # Output: Hello from inside!


# =============================================================================
# 11. CLOSURE
# =============================================================================
# Inner function that remembers values from outer function's scope


def multiplier(x):
    def multiply(y):
        return x * y

    return multiply


times_3 = multiplier(3)
print(times_3(10))  # Output: 30
print(times_3(5))  # Output: 15


# =============================================================================
# 12. HIGHER-ORDER FUNCTION
# =============================================================================
# Function that takes another function as parameter or returns a function


def apply_operation(func, value):
    return func(value)


def double(x):
    return x * 2


result = apply_operation(double, 5)
print(result)  # Output: 10


# =============================================================================
# 13. DECORATOR FUNCTION
# =============================================================================
# Function that modifies the behavior of another function


def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


@uppercase_decorator
def say_hello():
    return "hello world"


print(say_hello())  # Output: HELLO WORLD


# =============================================================================
# 14. GENERATOR FUNCTION
# =============================================================================
# Function that uses 'yield' instead of 'return' to generate values one at a time
# Memory efficient for large sequences


def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1


for num in count_up_to(5):
    print(num, end=" ")  # Output: 1 2 3 4 5
print()


# =============================================================================
# 15. FUNCTION WITH TYPE HINTS (Type Annotations)
# =============================================================================
# Specifies the expected types of parameters and return value


def add_numbers(a: int, b: int) -> int:
    return a + b


print(add_numbers(10, 20))  # Output: 30


# =============================================================================
# 16. FUNCTION WITH POSITIONAL-ONLY PARAMETERS (Python 3.8+)
# =============================================================================
# Parameters before '/' can only be passed by position


def divide(a, b, /):
    return a / b


print(divide(10, 2))  # Output: 5.0
# divide(a=10, b=2)  # This would raise an error