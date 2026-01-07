import numpy as np

val=np.array([1, 2, 3, 4, 5])
print("Array:", val)    
print("Data type:", val.dtype)
print("Number of dimensions:", val.ndim)

val2=np.array([1,2.0 , "3"])
print("\nArray with mixed types:", val2)    
print("Data type:", val2.dtype)

val3=np.linspace(0, 10, 5)
print("\nLinearly spaced array from 0 to 10 with 5 elements:", val3)

val4=np.arange(0, 20, 2)
print("\nArray with values from 0 to 20 with step 2:", val4)

val5=np.zeros((3, 4))
print("\n3x4 Array of zeros:\n", val5)

val6=np.ones((2, 5))
print("\n2x5 Array of ones:\n", val6)

val7=np.random.rand(3, 3)
print("\n3x3 Array of random values between 0 and 1:\n", val7)

val8=np.random.randint(0, 10, (4, 4))
print("\n4x4 Array of random integers between 0 and 10:\n", val8)

val9=np.full((2, 3), 7)
print("\n2x3 Array filled with 7:\n", val9)


# two dimensional array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array (Matrix):\n", matrix)

print("Shape of the matrix:", matrix.shape) 
print("Element at row 1, column 2:", matrix[1, 2])

# three dimensional array
tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array (Tensor):\n", tensor)