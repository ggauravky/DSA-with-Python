
# ! Recusive stack:

# A recursive stack is a data structure that stores information about the active subroutines or functions in a program during its execution.
# When a function is called, a new frame is added to the stack, containing information such as the function's parameters, local variables, and return address.
# When the function completes its execution, its frame is removed from the stack, and control is returned to the calling function.

# Example:
def recursive_function(n):
    # base case
    if n <= 0:
        return
    print(f"Entering level {n}")
    recursive_function(n - 1)
    print(f"Exiting level {n}")
recursive_function(5)
# In this example, each time recursive_function is called, a new frame is added to the stack.
# When the base case is reached, the function starts returning, and the frames are removed from the stack in reverse order.