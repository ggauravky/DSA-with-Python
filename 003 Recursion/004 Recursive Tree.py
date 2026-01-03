
#! Recursive Tree 

# A recursive tree is a data structure where each node can have multiple child nodes, and each child node can itself be the root of a subtree.
# This structure is often used to represent hierarchical data or to solve problems that can be broken down into smaller subproblems.
# Each node in the tree represents a function call, and the branches represent the recursive calls made by that function.

# Example:
# Diagram of a recursive tree for calculating factorial of 3:
#
#                    factorial(3)
#                        |
#                    factorial(2)
#                        |
#                    factorial(1)
#                        |
#                    factorial(0)
#                        |
#                       1

def factorial(n):
    # base case
    if n <= 0:
        return 1
    print(f"Calculating factorial({n})")
    result = n * factorial(n - 1)
    print(f"factorial({n}) = {result}")
    return result

factorial(3)

# fabionacci example
def fibonacci(n):
    # base case
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    print(f"Calculating fibonacci({n})")
    result = fibonacci(n - 1) + fibonacci(n - 2)
    print(f"fibonacci({n}) = {result}")
    return result

fibonacci(4)
# In this example, each call to factorial or fibonacci creates a new node in the recursive tree.
# The tree branches out with each recursive call until the base case is reached.