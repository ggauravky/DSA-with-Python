nums=[5,6,4,5,3,2,4,5,6,7,4,4,5,4,3,4,4,5,]

freq={}

for i in range(len(nums)):
    if nums[i] not in freq.keys():
        freq[nums[i]]=1
    else:
        freq[nums[i]]+=1


print(freq)

#time complexity is O(n) and space complexity is O(n)

#------------------------

# using get method

hashmap={}
n=len(nums)
for i in range(n):
    hashmap[nums[i]]=hashmap.get(nums[i],0)+1
print(hashmap)

#time complexity is O(n) and space complexity is O(n)

#------------------

# using collections module
from collections import Counter 
hashmap2=Counter(nums)
print(hashmap2)

#time complexity is O(n) and space complexity is O(n)