num=1221
rev=0
n=num
while n>0:
    digit=n%10
    rev=(rev*10)+(digit)
    n=n//10
    
print(rev)

if num==rev:
    print(True)
else:
    print(False)