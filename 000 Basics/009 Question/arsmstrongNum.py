num=1634

num1=num

len=0
while num1>0:
    len=len+1
    num1=num1//10

print(len)

num2=num

sum=0

while num2>0:
    digit=num2%10   
    digit=digit**len
    sum=sum+digit
    digit=0
    
    num2=num2//10

print(num2)
print(sum)

if num==sum:
    print(True)
else:
    print(False)