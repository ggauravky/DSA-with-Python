
#! 1. Question:
# print from 1 to n using loop and recursion

# using loop

n=5
i=1
while i<=n:
    # print(i)
    i+=1

# using recursion
def printNNum(i,n):
    # base case:
    if i>n:
        return
    
    # recursive case:
    print(i)
    printNNum(i+1,n)

# printNNum(1,5)


#! 2. Question:
# Print the factorial of a num

# using loops:
n=5
i=1
num=1

while(i<=5):
    # print(i)
    num=num*i
    i+=1

# print(num)

# using recursion:
def factorial(n):
    if (n==0) or (n==1):
        return 1
    return n*factorial(n-1)
a=factorial(5)
# print(a)