# character hashing

n=["a","b","c","d","e","f","g","h","i","j"]
m=["a","b","c","d","e","f","g","h","i","j"]

#constraints
#1. n[i] is a lowercase English letter
#2. n can have 10^6 elements
#3. m can have 10^6 elements

#1st method - brute force

for i in m:
    if i in n:
        print(i,"is present in the list")
    else:
        print(i,"is not present in the list")

#time complexity of the above method is O(n*m) which is not efficient for large values of n and m
#space complexity is O(1) as we are not using any extra space

#2nd method - using a hash list

hash_list=[0]*26
for i in n:
    hash_list[ord(i)-ord('a')]+=1
for i in m:
    if ord(i)-ord('a')<0 or ord(i)-ord('a')>25:
        print(i,"is not present in the list")
    else:
        print(hash_list[ord(i)-ord('a')],"is the count of",i,"in the list")
        
        
#time complexity of the above method is O(n+m) which is efficient for large values of n and m
#space complexity is O(1) as we are using a fixed size list of 26

#3rd method - using a hash dictionary
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
#space complexity is O(n) as we are using a dictionary to store the count of each character in the list