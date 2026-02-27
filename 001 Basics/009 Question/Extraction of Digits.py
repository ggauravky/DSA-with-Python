n=12345678910
l=0

while n>0:
    digit=n%10
    l=l+1
    n=n//10

print(l)