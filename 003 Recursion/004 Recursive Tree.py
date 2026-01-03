
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

