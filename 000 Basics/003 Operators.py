"""Basic examples of Python operators.

For each operator: one–line explanation, sample code, and expected output.
Run this file to see the actual printed outputs.
"""

print("\n===== Arithmetic Operators =====")

# + : Adds two values.
a = 10 + 5
print("10 + 5 =", a)  # Output: 15

# - : Subtracts right operand from left.
b = 10 - 5
print("10 - 5 =", b)  # Output: 5

# * : Multiplies two values.
c = 10 * 5
print("10 * 5 =", c)  # Output: 50

# / : Divides left by right (returns float).
d = 10 / 4
print("10 / 4 =", d)  # Output: 2.5

# // : Floor division (integer result, rounded down).
e = 10 // 4
print("10 // 4 =", e)  # Output: 2

# % : Modulus, remainder after division.
f = 10 % 4
print("10 % 4 =", f)  # Output: 2

# ** : Exponentiation (power).
g = 2**3
print("2 ** 3 =", g)  # Output: 8


print("\n===== Comparison (Relational) Operators =====")

x, y = 10, 20

# == : Checks if two values are equal.
print("10 == 20 ->", x == y)  # Output: False

# != : Checks if two values are not equal.
print("10 != 20 ->", x != y)  # Output: True

# > : Checks if left is greater than right.
print("10 > 20  ->", x > y)  # Output: False

# < : Checks if left is less than right.
print("10 < 20  ->", x < y)  # Output: True

# >= : Checks if left is greater than or equal to right.
print("10 >= 20 ->", x >= y)  # Output: False

# <= : Checks if left is less than or equal to right.
print("10 <= 20 ->", x <= y)  # Output: True


print("\n===== Logical Operators =====")

p, q = True, False

# and : True if both operands are True.
print("True and False ->", p and q)  # Output: False

# or : True if at least one operand is True.
print("True or False  ->", p or q)  # Output: True

# not : Inverts the boolean value.
print("not True      ->", not p)  # Output: False


print("\n===== Bitwise Operators (work on bits) =====")

m, n = 5, 3  # 5 -> 0101, 3 -> 0011 in binary

# & : Bitwise AND (1 only when both bits are 1).
print("5 & 3  =", m & n)  # 0101 & 0011 -> 0001 (1)

# | : Bitwise OR (1 when at least one bit is 1).
print("5 | 3  =", m | n)  # 0101 | 0011 -> 0111 (7)

# ^ : Bitwise XOR (1 when bits are different).
print("5 ^ 3  =", m ^ n)  # 0101 ^ 0011 -> 0110 (6)

# ~ : Bitwise NOT (flips all bits, works as -x-1 in two's complement).
print("~5    =", ~m)  # Output: -6

# << : Left shift (moves bits left, fills with 0 on right).
print("5 << 1 =", m << 1)  # 0101 << 1 -> 1010 (10)

# >> : Right shift (moves bits right, may drop bits on right).
print("5 >> 1 =", m >> 1)  # 0101 >> 1 -> 0010 (2)


print("\n===== Assignment Operators =====")

# = : Simple assignment.
num = 10
print("num =", num)  # Output: 10

# += : Adds right value to variable and assigns back.
num += 5  # num = num + 5
print("num += 5 ->", num)  # Output: 15

# -= : Subtracts right value from variable and assigns back.
num -= 3  # num = num - 3
print("num -= 3 ->", num)  # Output: 12

# *= : Multiplies variable by right value and assigns back.
num *= 2  # num = num * 2
print("num *= 2 ->", num)  # Output: 24

# /= : Divides variable by right value and assigns back (float).
num /= 4  # num = num / 4
print("num /= 4 ->", num)  # Output: 6.0

# //= : Floor-divides variable by right value and assigns back.
num //= 5  # num = num // 5
print("num //= 5 ->", num)  # Output: 1.0

# %= : Stores remainder after division.
num %= 2  # num = num % 2
print("num %= 2 ->", num)  # Output: 1.0

# **= : Raises variable to power of right value.
num **= 3  # num = num ** 3
print("num **= 3 ->", num)  # Output: 1.0


print("\n===== Membership Operators =====")

lst = [1, 2, 3, 4]

# in : True if value is present in a sequence.
print("2 in [1, 2, 3, 4]   ->", 2 in lst)  # Output: True

# not in : True if value is NOT present in a sequence.
print("5 not in [1, 2, 3, 4] ->", 5 not in lst)  # Output: True


print("\n===== Identity Operators =====")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# is : True if both variables refer to the same object.
print("list1 is list3 ->", list1 is list3)  # Output: True
print(
    "list1 is list2 ->", list1 is list2
)  # Output: False (same value, different objects)

# is not : True if variables do NOT refer to the same object.
print("list1 is not list2 ->", list1 is not list2)  # Output: True


print("\n===== Mixed Example =====")

# Small combined example using arithmetic, comparison, and logical operators.
age = 18
marks = 75

# Check if someone is an adult AND has marks greater than 60.
result = (age >= 18) and (marks > 60)
print("(age >= 18) and (marks > 60) ->", result)  # Output: True
