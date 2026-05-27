#number hashing


n=[5,3,2,2,1,5,3,4,5,6,7,8,9,10]
m=[10,2,1,3,4,5,6,7,8,9]

#constraints
#1. 1<=n[i]<=10
#2.n can have 10^6 elements
#3. m can have 10^6 elements


#1st method

for i in m:
    if i in n:
        print(i,"is present in the list")
    else:
        print(i,"is not present in the list")
        
#time complexity of the above method is O(n*m) which is not efficient for large values of n and m
#space complexity is O(1) as we are not using any extra space
        
#2nd method

hash_list=[0]*11
for i in n:
    hash_list[i]+=1

for i in m:
    if i<1 and i>10:
        print(i,"is not present in the list")
    else:
        print(hash_list[i],"is the count of",i,"in the list")
        
#time complexity of the above method is O(n+m) which is efficient for large values of n and m
#space complexity is O(1) as we are using a fixed size list of 11
        

#3rd method

hash_dict={}
for i in n:
    if i in hash_dict:
        hash_dict[i]+=1
    else:
        hash_dict[i]=1
    
for i in m:
    if i in hash_dict:
        print(hash_dict[i],"is the count of",i,"in the list")
    else:
        print(i,"is not present in the list")
        
#time complexity of the above method is O(n+m) which is efficient for large values of n and m
#space complexity is O(n) as we are using a dictionary to store the count of each