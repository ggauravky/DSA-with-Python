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

#