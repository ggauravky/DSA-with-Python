# loop vs Recursion

# /in table form

# !| Aspect               | Loop                              | Recursion                         |
# |----------------------|-----------------------------------|-----------------------------------|  
# | Definition           | A control flow statement that     | A function that calls itself to   |
# |                      | repeatedly executes a block of    | solve a problem by breaking it    |
# |                      | code while a condition is true.   | down into smaller subproblems.   |
# | Use Cases            | Iterating over collections,       | Solving problems that can be     |
# |                      | performing repetitive tasks,     | defined in terms of smaller      |    
#                     | and implementing algorithms      | instances of the same problem,   |
#                      | like searching and sorting.      | such as factorial calculation,   |
#                      |                                   | Fibonacci sequence, and tree     |
#                      |                                   | traversals.                      |
# | Memory Usage         | Generally uses less memory as it  | Can lead to higher memory usage due  |   
# |                      | maintains a single stack frame.   | to multiple stack frames for each  |
# |                      |                                   | recursive call.                  |
# | Readability          | Can be less readable for complex  | Often more readable and easier to  |
# |                      | tasks due to nested loops.       | understand for problems that are  |   
#                      |                                   | naturally recursive.             |
# | Performance          | Typically faster for simple       | Can be slower due to function    |   
# |                      | iterations as it avoids the       | call overhead and potential stack  |
#                      | overhead of function calls.       | overflow for deep recursion.     |
# | Tail Call Optimization | Not applicable.                  | Some languages support tail call  |
# |                      |                                   | optimization to improve performance|
#                      |                                   | for certain types of recursion.   |
# | Examples             | for loops, while loops, foreach   | Factorial calculation, Fibonacci  |
# |                      | loops.                            | sequence, tree traversals.       |
# | Language Support     | Supported in all programming      | Supported in most programming     |
# |                      | languages.                       | languages, but with varying       |
#                      |                                   | levels of optimization.          |
# | Debugging            | Easier to debug as the flow of    | Can be harder to debug due to    |
# |                      | control is explicit.             | multiple function calls and stack |
#                      |                                   | frames.                          |

# looops
def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial_loop(5))  # Output: 120

# recursion
def factorial_recursion(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)
print(factorial_recursion(5))  # Output: 120

# Both functions calculate the factorial of a number using different approaches.
