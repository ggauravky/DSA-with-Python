
#! Time Complexity :

# Time complexity is a computational complexity that describes the amount of time it takes to run an algorithm as a function of the length of the input. It provides an estimate of the running time

# The time complexity of this function is O(n), where n is the length of the input list 'arr'.
# This is because the function iterates through the list once to find the maximum value, 
# performing a constant-time comparison for each element.

#! Asymptotic Notations:

#* 1. Big O Notation (O): It describes the upper bound of the time complexity, representing the worst-case scenario.

#* 2. Omega Notation (Ω): It describes the lower bound of the time complexity, representing the best-case scenario.

#* 3. Theta Notation (Θ): It describes the exact bound of the time complexity, representing both the upper and lower bounds.

# ! Types of Time Complexities:

#* 1.linear time complexity O(n)

for i in range(10):  # O(1)
    print(i)  # O(1)
    
# Overall time complexity: O(1) + O(1) = O(2) = O(1)

#* 2.Constant time complexity O(1)

for i in range(100):  # O(n)
    print(i)  # O(1)
    
# Overall time complexity: O(n) * O(1) = O(n)

#* 3.Quadratic time complexity O(n^2)

for i in range(10):  # O(n)
    for j in range(10):  # O(n)
        print(i, j)  # O(1)

# Overall time complexity: O(n) * O(n) * O(1) = O(n^2)

#* 4.Logarithmic time complexity O(log n)

i=1
n=1000
while i < n:  # O(log n)
    print(i)  # O(1)
    i = i * 2
    
# Overall time complexity: O(log n) * O(1) = O(log n)

#* 5. Exponential time complexity O(2^n)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2) 
n = 5
print(fibonacci(n))  # O(2^n)
# Overall time complexity: O(2^n)

#* 6. Linearithmic time complexity O(n log n)

n=1000
for i in range(n):  # O(n)
    j = 1
    while j < n:  # O(log n)
        print(i, j)  # O(1)
        j = j * 2   

# Overall time complexity: O(n) * O(log n) * O(1) = O(n log n)
    
#* 7. Factorial time complexity O(n!)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = 5
print(factorial(n))  # O(n!)

# Overall time complexity: O(n!)

#* Cubic time complexity O(n^3)

n = 10
for i in range(n):  # O(n)
    for j in range(n):  # O(n)
        for k in range(n):  # O(n)
            print(i, j, k)  # O(1)

# Overall time complexity: O(n) * O(n) * O(n) * O(1) = O(n^3)


#! Common Time Complexities in Order from Fastest to Slowest:
# 1. O(1) - Constant Time
# 2. O(log n) - Logarithmic Time
# 3. O(n) - Linear Time
# 4. O(n log n) - Linearithmic Time
# 5. O(n^2) - Quadratic Time
# 6. O(n^3) - Cubic Time
# 7. O(2^n) - Exponential Time
# 8. O(n!) - Factorial Time

#! Note:
# The actual time taken by an algorithm can depend on various factors such as hardware, programming language, and compiler optimizations. Time complexity provides a high-level understanding of an algorithm's efficiency, but real-world performance may vary.

# from higher to lower Time Complexity:
# O(n!) > O(2^n) > O(n^3) > O (n^2) > O(n log n) > O(n) > O(log n) > O(1)