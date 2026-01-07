import array

#! Creating an array of integers
int_array = array.array('i', [1, 2, 3, 4, 5])
print("Integer Array:", int_array)
#! Accessing elements
print("First Element:", int_array[0])

#! Creating an array of floats
float_array = array.array('f', [1.1, 2.2, 3.3])
print("Float Array:", float_array)  

#! printing elements using loop
for element in float_array:
    print("Element:", element)
    
for i in range(len(int_array)):
    print("Element at index", i, ":", int_array[i])
    
#! charactre code:
# 'i' - signed integer - 2 bytes
# 'f' - float - 4 bytes
# 'b' - signed char - 1 byte
# 'd' - double - 8 bytes
# 'b' - signed char - 1 byte
# 'B' - unsigned char - 1 byte
# 'c' - char - 1 byte
# 's' - signed short - 2 bytes

print(int_array.typecode)  # Output: 'i'

#! Modifying an element
int_array[2] = 10
print("Modified Integer Array:", int_array)

#! Appending an element
int_array.append(6)
int_array.extend([7, 8, 9])
int_array.insert(0, 0)
print("Appended Integer Array:", int_array)

#! Removing elements
int_array.remove(10)  # Remove first occurrence of 10
popped_element = int_array.pop()  # Remove and return last element
int_array.pop(0)  # Remove element at index 0
print("After Removal Integer Array:", int_array)
print("Popped Element:", popped_element)

#! copying array
copy_Array=array.array(int_array.typecode,int_array)
print("Copied Array:",copy_Array)

copy_Array2=int_array[:]
print("Copied Array 2:",copy_Array2)

#! copy using fromlist
list_to_copy=[20,21,22]
copy_Array3=array.array(int_array.typecode)
copy_Array3.fromlist(list_to_copy)  
print("Copied Array 3 from list:",copy_Array3)

#! Converting array to list
array_as_list = int_array.tolist()
print("Array as List:", array_as_list)

#! Getting the length of the array
print("Length of Integer Array:", len(int_array))

#! Finding the index of an element
index_of_4 = int_array.index(4)
print("Index of element 4:", index_of_4)

#! Reversing the array
int_array.reverse()
print("Reversed Integer Array:", int_array)

#! slicing
sliced_array = int_array[2:5]   
print("Sliced Array (index 2 to 4):", sliced_array)

#! all slices
print("Array from index 3 to end:", int_array[3:])
print("Array from start to index 4:", int_array[:5])
print("Array with step 2:", int_array[::2])
print("Array reversed using slicing:", int_array[::-1])
print("Array from index 5 to 2 with step -1:", int_array[5:2:-1])
print("Array from index 5 to 0 with step -2:", int_array[5::-2])

# taking input from user to create an array
size = int(input("Enter the size of the array: "))
user_array = array.array('i')  # Creating an empty array of integers
for i in range(size):
    element = int(input(f"Enter element {i + 1}: "))
    user_array.append(element)
    
print("User Created Array:", user_array)
