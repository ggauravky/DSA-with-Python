
# ! Space Complexity :

# Space complexity refers to the amount of memory an algorithm uses in relation to the size of the input data. It is expressed using Big O notation, similar to time complexity.

#! Example:
def example_space_complexity(n):
    # O(1) Space Complexity: Using a fixed amount of space
    constant_space = 10  # This uses a constant amount of space regardless of input size

    # O(n) Space Complexity: Using space proportional to the input size
    linear_space = [0] * n  # This creates a list of size n

    # O(n^2) Space Complexity: Using space proportional to the square of the input size
    matrix_space = [[0] * n for _ in range(n)]  # This creates an n x n matrix

    return constant_space, linear_space, matrix_space

n = 5
constant_space, linear_space, matrix_space = example_space_complexity(n)
print("Constant Space:", constant_space)
print("Linear Space:", linear_space)
print("Matrix Space:", matrix_space)

#! In this example:
#* The variable 'constant_space' uses O(1) space.
#* The list 'linear_space' uses O(n) space.
#* The matrix 'matrix_space' uses O(n^2) space.
#* Overall Space Complexity: O(1) + O(n) + O(n^2) = O(n^2)


    