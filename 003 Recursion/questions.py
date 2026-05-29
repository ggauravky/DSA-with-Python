#print 10 , 3 times using recursion

def print_numbers(n):
    if n == 0:
        return
    print(10)
    print_numbers(n - 1)

print_numbers(3)

#print 1 to n using recursion

def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)
print_numbers(5)

#sum of 1 to n using recursion :

def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)

print(sum(5))

#reverse an array using recursion

def reverse_array(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array(arr, start + 1, end - 1)
    
arr = [1, 2, 3, 4, 5]
reverse_array(arr, 0, len(arr) - 1)
print(arr)

#reverse an array using loops (taking 2 pointers)
def reverse_array_loops(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

arr = [1, 2, 3, 4, 5]
print(reverse_array_loops(arr))
