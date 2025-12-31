"""Basic examples of Python data types.
For each data type: one–line explanation, sample code, and expected output.
Run this file to see the actual printed outputs.
"""

print("\n===== Numeric Types =====")    
# int : Integer type.
a = 42  
print("Integer a =", a)  # Output: 42
print("Type of a:", type(a))  # Output: <class 'int'>
# float : Floating-point type.
b = 3.14
print("Float b =", b)  # Output: 3.14
print("Type of b:", type(b))  # Output: <class 'float'>
# complex : Complex number type.
c = 1 + 2j
print("Complex c =", c)  # Output: (1+2j)
print("Type of c:", type(c))  # Output: <class 'complex'>


print("\n===== Text Type =====")
# str : String type.
s = "Hello, World!"
print("String s =", s)  # Output: Hello, World!
print("Type of s:", type(s))  # Output: <class 'str'>


print("\n===== Sequence Types =====")
# list : List type (ordered, mutable).
lst = [1, 2, 3, 4, 5]
print("List lst =", lst)  # Output: [1, 2, 3
print("Type of lst:", type(lst))  # Output: <class 'list'>
# tuple : Tuple type (ordered, immutable).
tup = (1, 2, 3, 4, 5)
print("Tuple tup =", tup)  # Output: (1, 2, 3
print("Type of tup:", type(tup))  # Output: <class 'tuple'>
# range : Range type (immutable sequence of numbers).
rng = range(1, 6)
print("Range rng =", list(rng))  # Output: [1, 2, 3, 4, 5]
print("Type of rng:", type(rng))  # Output: <class 'range'>


print("\n===== Mapping Type =====")
# dict : Dictionary type (key-value pairs).
dct = {"name": "Alice", "age": 30}
print("Dictionary dct =", dct)  # Output: {'name': 'Alice', 'age': 30}
print("Type of dct:", type(dct))  # Output: <class 'dict'>


print("\n===== Set Types =====")
# set : Set type (unordered, unique elements).
st = {1, 2, 3, 4, 5}
print("Set st =", st)  # Output: {1, 2, 3, 4, 5}
print("Type of st:", type(st))  # Output: <class 'set'>
# frozenset : Immutable set type.
frz_st = frozenset([1, 2, 3, 4, 5])
print("Frozenset frz_st =", frz_st)  # Output: frozenset({1, 2, 3, 4, 5})
print("Type of frz_st:", type(frz_st))  # Output: <class 'frozenset'>


print("\n===== Boolean Type =====")
# bool : Boolean type (True or False).
flag = True
print("Boolean flag =", flag)  # Output: True
print("Type of flag:", type(flag))  # Output: <class 'bool'>


print("\n===== Binary Types =====")
# bytes : Immutable sequence of bytes.
bts = b"Hello"
print("Bytes bts =", bts)  # Output: b'Hello'
print("Type of bts:", type(bts))  # Output: <class 'bytes'>
# bytearray : Mutable sequence of bytes.    
barr = bytearray(b"Hello")
print("Bytearray barr =", barr)  # Output: bytearray(b'Hello')
print("Type of barr:", type(barr))  # Output: <class 'bytearray'>
# memoryview : Memory view object of a bytes-like object.
mem_view = memoryview(b"Hello")
print("Memoryview mem_view =", mem_view)  # Output: <memory at ...>
print("Type of mem_view:", type(mem_view))  # Output: <class 'memoryview'>


print("\n===== None Type =====")
# NoneType : Represents the absence of a value.
none_var = None
print("NoneType none_var =", none_var)  # Output: None
print("Type of none_var:", type(none_var))  # Output: <class 'NoneType'>


print("\n===== Summary =====")
print("Numeric Types: int, float, complex")
print("Text Type: str")
print("Sequence Types: list, tuple, range")
print("Mapping Type: dict")
print("Set Types: set, frozenset")
print("Boolean Type: bool")
print("Binary Types: bytes, bytearray, memoryview")
print("None Type: NoneType")
print("These are the fundamental data types in Python used to store and manipulate data.")
