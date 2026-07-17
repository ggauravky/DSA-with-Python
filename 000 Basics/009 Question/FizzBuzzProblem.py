# Fizz Buzz

# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

n=5
output=[]

for i in range(1 , n+1):
    if i%3 ==0 and i%5==0:
        output.append("FizzBuzz")
    elif i%3==0:
        output.append("Fizz")
    elif i%5==0:
        output.append("Buzz")
    else:
        output.append(str(i))
        
print(output)